import requests
import random
import time
import base64
import re
import string
from typing import Dict, List, Optional

class LinkGeneratorChecker:
    """
    链接生成与检测工具类
    
    该类提供了生成随机链接并检测其可用性的功能，
    支持自定义单词列表或随机字符串生成子域名，
    包含主要域名和备用域名两套系统，在主要链接不足时会自动补充备用链接。
    """
    
    def __init__(self, 
                 words: Optional[List[str]] = None, 
                 use_random_string: bool = False,
                 string_length: int = 6):
        """
        初始化链接生成器
        
        参数:
            words: 自定义单词列表，默认为None使用内置列表
            use_random_string: 是否使用随机字符串代替单词，默认为False
            string_length: 随机字符串长度，默认为6个字符
        """
        # 内置单词列表（如果未提供自定义列表则使用）
        self._default_words = ['abandon', 'ability', 'able', 'above', 'abroad', 'absence', 
                              'absorb', 'abuse', 'accept', 'access', 'account', 'accuse', 
                              'achieve', 'acid', 'acquire', 'across', 'act', 'action', 
                              'active', 'actor']
        
        # 保存配置参数
        self.use_random_string = use_random_string
        self.string_length = string_length
        
        # 设置单词列表（优先使用用户提供的列表）
        self.words = words if words is not None else self._default_words
        self.domain = self.extract_specific_domains()
        # 主要域名和备用域名
        self.main_domain = self.domain[0][1::]
        self.backup_domain = self.domain[1][1::]
        
        
    def extract_specific_domains(self):
        """
        从HTML代码中提取特定位置的域名后缀（如.utnfpqze.top和.vcxgpzzg.me）
        这些域名后缀位于JavaScript代码的words.random() + '之后、'});之前
        
        参数:
        html_code (str): 包含目标模式的HTML代码
        
        返回:
        list: 匹配到的域名后缀列表，若未找到则返回默认列表[.utnfpqze.top, .vcxgpzzg.me]
        """
        # 正则表达式模式：精准匹配位于words.random() + '之后、'});之前的域名后缀
        # 模式说明：
        # - 匹配固定前缀：words\.random\(\) \+ '
        # - 捕获域名后缀：(\.[a-zA-Z0-9-]+\.[a-zA-Z]{2,}) （以.开头，包含字母数字横线，最后是2个以上字母的顶级域名）
        # - 匹配固定后缀：'\);
        html_code = self.get_domain_html_text()
        default_domain = ['.utnfpqze.top', '.vcxgpzzg.me']

        new_domain = []

        dyg = re.findall(r"return location.protocol \+ '//' \+ words.random\(\) \+ '(.*?)'    \}\);",html_code )
        if dyg:
            new_domain.append(dyg[0].strip())

        drg = re.findall(r"\+words.random\(\)\+'(.*?)';",html_code )
        if drg:
            new_domain.append(drg[0].strip())
        if len(new_domain) > 0:
            return new_domain
        else:
            return default_domain
    
    # 获取域名
    def get_domain_html_text(self):
        html_text =  base64.b64decode(requests.get("https://www.ulvlinv.xyz/").text.split("document.write(Base64.decode('")[-1].split("'));")[0]).decode('utf-8')
        return html_text

    def add_words(self, new_words: List[str]) -> None:
        """
        向单词列表添加新单词
        
        参数:
            new_words: 要添加的新单词列表
        """
        self.words.extend(new_words)
        # 去重处理
        self.words = list(set(self.words))

    def _generate_random_subdomain(self) -> str:
        """生成随机字符串子域名"""
        # 只包含小写字母的随机字符串
        return ''.join(random.choices(string.ascii_lowercase, k=self.string_length))

    def generate_links(self, count: int = 3) -> Dict[str, List[str]]:
        """
        生成随机链接
        
        参数:
            count: 需要生成的链接数量（主域名和备用域名各生成此数量）
            
        返回:
            包含主域名链接列表和备用域名链接列表的字典
        """
        main_links = []
        backup_links = []
        
        # 生成链接的逻辑
        for _ in range(count):
            # 根据配置决定使用单词还是随机字符串
            if self.use_random_string:
                subdomain = self._generate_random_subdomain()
            else:
                subdomain = random.choice(self.words)
                
            main_links.append(f'https://{subdomain}.{self.main_domain}')
            
        for _ in range(count):
            if self.use_random_string:
                subdomain = self._generate_random_subdomain()
            else:
                subdomain = random.choice(self.words)
                
            backup_links.append(f'https://{subdomain}.{self.backup_domain}')
        
        return {'main_links': main_links, 'backup_links': backup_links}

    def check_link(self, url: str) -> bool:
        """检测单个链接的可用性（保持原有逻辑不变）"""
        try:
            response = requests.head(url, allow_redirects=True)
            return response.status_code < 400
        except (requests.RequestException, ValueError):
            return False

    def check_multiple_links(self, links: List[str]) -> List[str]:
        """批量检测链接可用性（保持原有逻辑不变）"""
        results = []
        for link in links:
            if self.check_link(link):
                results.append(link)
            time.sleep(0.5)
        return results

    def generate_and_check_links(self, link_count: int = 3) -> Dict[str, object]:
        """主功能：生成并检测链接（保持原有逻辑不变）"""
        try:
            links = self.generate_links(link_count)
            main_links = links['main_links']
            backup_links = links['backup_links']
            
            available_main_links = self.check_multiple_links(main_links)
            
            if len(available_main_links) < link_count:
                needed = link_count - len(available_main_links)
                available_backup_links = self.check_multiple_links(backup_links[:needed])
                available_main_links.extend(available_backup_links)
            
            return {
                'is_available': len(available_main_links) > 0,
                'available_links': available_main_links
            }
        except Exception as e:
            print(f"链接生成与检测过程中出错: {e}")
            return {
                'is_available': False,
                'available_links': []
            }

# 示例用法
if __name__ == "__main__":
    # 示例 2：使用自定义单词列表
    custom_words = ['BloodSpider', 'BloodSpiderAV', 'asfef']
    checker2 = LinkGeneratorChecker(words=custom_words)
    result2 = checker2.generate_and_check_links()
    print("\n示例 2：使用自定义单词列表")
    print(f"是否有可用链接: {result2['is_available']}")
    print(f"可用链接列表: {result2['available_links']}")
