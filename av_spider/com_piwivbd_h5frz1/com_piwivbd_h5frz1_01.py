import requests
import re
from lxml import etree
import json
from BloodSpiderModel.spider_tools.common_utils import GeneralToolkit
from BloodSpiderModel.spider_tools.file_operate import FileOperate
from av_spider.com_piwivbd_h5frz1.get_base_url import LinkGeneratorChecker

base_urls = LinkGeneratorChecker(words=['BloodSpider', 'BloodSpiderAV', 'asfef'])


class PiwivbdH5frz1:
    def __init__(self, debug: bool = True) -> None:
        self.debug = debug
        self.json_config_file_path = "link_config.json"
        self.file_operate = FileOperate()
        self.base_url = self._get_base_url()
        self.headers = {
            'Referer': self.base_url,
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        }
        self.common_utils = GeneralToolkit()

        # 敏感词列表
        self.sensitive_words = [
            "51爆料网",
            "51"
        ]

    def _get_base_url(self):
        if self.debug is False:
            print("走我")
            # 手动获取最新地址
            result2 = base_urls.generate_and_check_links(1)
            dqsj = json.loads(self.file_operate.read_file(self.json_config_file_path))
            with open(self.json_config_file_path, "w", encoding='utf-8') as f:
                # 更新数据
                dqsj[0]['available_links'] = result2['available_links']
                f.write(json.dumps(dqsj, ensure_ascii=False))
        else:

            result2 = json.loads(self.file_operate.read_file("link_config.json"))[0]
        return result2['available_links'][0]

    # 负责发起请求并返回: 原html文本 | etree_HTML转换后的文本
    def _fetch_html_content(self, url):
        html_text = requests.get(f'{url}', headers=self.headers).text
        # html_text = open(url, "r", encoding="utf-8").read()
        etree_text = etree.HTML(html_text)
        return html_text, etree_text

        # 获取吃瓜列表的分页数据

    def _fetch_paginated_melon_list(self, chi_gua_ye_mian):
        feye_info = chi_gua_ye_mian.xpath("//*[@id='pageForm']/span/text()")
        if not feye_info:
            return {
                "chi_gua_lie_biao_fe_ye_dang_qian_ye": 0,
                "chi_gua_lie_biao_fe_ye_zo_fe_ye": 0,
            }

        feye_info = str(feye_info[0]).split("/")
        return {
            "chi_gua_lie_biao_fe_ye_dang_qian_ye": feye_info[0].strip(),
            "chi_gua_lie_biao_fe_ye_zo_fe_ye": feye_info[1].strip(),
        }

    # 获取吃瓜总分类
    def Classification_of_Eating_Melons(self):
        html_text, etree_text = self._fetch_html_content(self.base_url)
        # 获取分类
        classification_lis = etree_text.xpath("//ul[@id='menu-menu-1']/li[2]//ul[@class='list']/li")
        classifications = []
        for li in classification_lis:
            classifications.append({
                "chi_gua_zo_fe_lei_fe_lei_id": self.base_url + li.xpath("./a/@href")[0],
                "chi_gua_zo_fe_lei_fe_lei_ming": li.xpath("./a/text()")[0],
            })
        return classifications

    # 获取吃瓜总分类:缓存版
    def get_gossip_total_categories_cached(self):

        return [
            {
                "chi_gua_zo_fe_lei_fe_lei_id": "https://h5frz1.piwivbd.com/category/jrbl/",
                "chi_gua_zo_fe_lei_fe_lei_ming": "今日爆料"
            },
            {
                "chi_gua_zo_fe_lei_fe_lei_id": "https://h5frz1.piwivbd.com/category/xsxy/",
                "chi_gua_zo_fe_lei_fe_lei_ming": "学生校园"
            },
            {
                "chi_gua_zo_fe_lei_fe_lei_id": "https://h5frz1.piwivbd.com/category/mxhl/",
                "chi_gua_zo_fe_lei_fe_lei_ming": "明星黑料"
            },
            {
                "chi_gua_zo_fe_lei_fe_lei_id": "https://h5frz1.piwivbd.com/category/fccg/",
                "chi_gua_zo_fe_lei_fe_lei_ming": "反差吃瓜"
            },
            {
                "chi_gua_zo_fe_lei_fe_lei_id": "https://h5frz1.piwivbd.com/category/bljp/",
                "chi_gua_zo_fe_lei_fe_lei_ming": "必撸精品"
            },
            {
                "chi_gua_zo_fe_lei_fe_lei_id": "https://h5frz1.piwivbd.com/category/mrds/",
                "chi_gua_zo_fe_lei_fe_lei_ming": "每日大赛"
            },
            {
                "chi_gua_zo_fe_lei_fe_lei_id": "https://h5frz1.piwivbd.com/category/cgxw/",
                "chi_gua_zo_fe_lei_fe_lei_ming": "吃瓜新闻"
            },
            {
                "chi_gua_zo_fe_lei_fe_lei_id": "https://h5frz1.piwivbd.com/category/rmdj/",
                "chi_gua_zo_fe_lei_fe_lei_ming": "热门短剧"
            },
            {
                "chi_gua_zo_fe_lei_fe_lei_id": "https://h5frz1.piwivbd.com/category/dyfjx/",
                "chi_gua_zo_fe_lei_fe_lei_ming": "抖音风精选"
            },
            {
                "chi_gua_zo_fe_lei_fe_lei_id": "https://h5frz1.piwivbd.com/category/hjll/",
                "chi_gua_zo_fe_lei_fe_lei_ming": "海角乱伦"
            },
            {
                "chi_gua_zo_fe_lei_fe_lei_id": "https://h5frz1.piwivbd.com/category/dmwm/",
                "chi_gua_zo_fe_lei_fe_lei_ming": "动漫无码"
            },
            {
                "chi_gua_zo_fe_lei_fe_lei_id": "https://h5frz1.piwivbd.com/category/cztz/",
                "chi_gua_zo_fe_lei_fe_lei_ming": "寸止挑战"
            },
            {
                "chi_gua_zo_fe_lei_fe_lei_id": "https://h5frz1.piwivbd.com/category/rmdg/",
                "chi_gua_zo_fe_lei_fe_lei_ming": "热门大瓜"
            },
            {
                "chi_gua_zo_fe_lei_fe_lei_id": "https://h5frz1.piwivbd.com/category/wmav/",
                "chi_gua_zo_fe_lei_fe_lei_ming": "无码AV"
            },
            {
                "chi_gua_zo_fe_lei_fe_lei_id": "https://h5frz1.piwivbd.com/category/whzq/",
                "chi_gua_zo_fe_lei_fe_lei_ming": "网黄专区"
            },
            {
                "chi_gua_zo_fe_lei_fe_lei_id": "https://h5frz1.piwivbd.com/category/thjp/",
                "chi_gua_zo_fe_lei_fe_lei_ming": "探花精选"
            },
            {
                "chi_gua_zo_fe_lei_fe_lei_id": "https://h5frz1.piwivbd.com/category/bkdg/",
                "chi_gua_zo_fe_lei_fe_lei_ming": "必看大瓜"
            }
        ]

    # 获取吃瓜列表
    def get_gossip_list(
            self,
            gossip_list_url: str = None
    ):

        if gossip_list_url is None or gossip_list_url == "undefined":
            gossip_list_url = self.base_url
        else:
            gossip_list_url = gossip_list_url.strip()

        html_text, etree_text = self._fetch_html_content(gossip_list_url)
        # 分页数据
        chi_gua_lie_biao_fe_ye = self._fetch_paginated_melon_list(etree_text)

        archives = etree_text.xpath("//*[@id='archive']")
        if not archives:
            archives = etree_text.xpath("//*[@id='index']")

        archives = archives[0].xpath("./article")
        # 吃瓜列表
        chi_gua_lie_biao = []
        for archive in archives:
            # 判断是不是广告
            if not archive.xpath("./a/div/div[2]/div/h2/text()"):
                continue
            elif not archive.xpath("./a/div/div[2]/div/h2/text()")[0].strip():
                continue
            # 标题
            chi_gua_lie_biao_biao_ti = str(archive.xpath("./a/div/div[2]/div/h2/text()")[0].strip()).replace("\n", "")

            # 吃瓜详情页链接
            if self.common_utils.check_common_substrings(archive.xpath("./a/@href")[0], ['https', 'http']) is False:
                chi_guo_xiang_qing_ye_url = self.base_url + archive.xpath("./a/@href")[0]
            else:
                chi_guo_xiang_qing_ye_url = archive.xpath("./a/@href")[0]

            # 获取吃瓜列表的封面图
            urls = re.findall(r"'(https?://[^']+)'", str(archive.xpath("./a/div/script/text()")[0]))
            if urls:
                chi_gua_lie_biao_cover = urls[0]
            else:
                chi_gua_lie_biao_cover = "https://pic.duofyi.cn/upload_01/xiao/20250701/2025070117460534378.jpeg"

            chi_gua_lie_biao.append({
                "chi_gua_lie_biao_biao_ti": chi_gua_lie_biao_biao_ti,
                "chi_guo_xiang_qing_ye_url": chi_guo_xiang_qing_ye_url,
                "chi_gua_lie_biao_cover": chi_gua_lie_biao_cover
            })

        # 当前页面的位置标题
        blog_title = self.common_utils.filter_sensitive_words(self.sensitive_words, str(
            etree_text.xpath("//*[@class='blog-title']/text()")[0]).strip(), "蜘蛛爆料网")

        return {
            "chi_gua_lie_biao": chi_gua_lie_biao,
            "chi_gua_lie_biao_fe_ye": chi_gua_lie_biao_fe_ye,
            "base_url": self.base_url,
            "blog_title": blog_title
        }

    # 获取吃瓜详情内容数据
    def get_gossip_detail_data(self, detail_url: str = r"av_spider\com_piwivbd_h5frz1\详情.html"):
        # 不需要的文章内容
        filtered_article_text: list = ["下载", "51", "关键词"]

        shi_fo_wei_chi_gua_xiang_qing_lie_biao_he_ji: bool = False

        html_text, etree_text = self._fetch_html_content(detail_url)

        # 标题
        chi_gua_lie_biao_biao_ti = etree_text.xpath("//*[@class='post-title ']/text() | //*[@class='post']/h1/text()")[
            0]

        # 上线时间
        chi_gua_lie_biao_shang_xian_shi_jian = etree_text.xpath("//*[@class='post-meta']/li[2]/time/text()")[0]

        # 整体内容
        post_content = etree_text.xpath("//*[@id='post']//*[@class='post-content']")[0]

        ps = post_content.xpath('./p')

        # 文章内容
        chi_guo_xiang_qing_nei_ro = ""

        # 吃瓜新闻详情内容的全部照片
        chi_gua_xiang_qing_zhao_pian_lie_biao = []
        for img in post_content.xpath(".//img"):
            chi_gua_xiang_qing_zhao_pian_lie_biao.append(img.xpath("./@data-xkrkllgl")[0])
        # 吃瓜合集列表
        chi_gua_lie_biao = []
        i = -1
        for p in ps:
            i += 1
            chi_guo_xiang_qing_nei_ro_item = p.xpath(".//text()")
            if len(chi_guo_xiang_qing_nei_ro_item) > 0:
                chi_gua_lie_biao_xiang_qing_nei_ro = chi_guo_xiang_qing_nei_ro_item
                chi_guo_xiang_qing_nei_ro_item = str(chi_guo_xiang_qing_nei_ro_item[0])

                # 有可能是文章
                if self.common_utils.check_common_substrings(chi_guo_xiang_qing_nei_ro_item, filtered_article_text):
                    continue
                elif len(p.xpath("./a")) >= 1:
                    # 列表详情中的合集
                    if shi_fo_wei_chi_gua_xiang_qing_lie_biao_he_ji is False:
                        shi_fo_wei_chi_gua_xiang_qing_lie_biao_he_ji = True

                    chi_gua_lie_biao_zi_dian = {
                        "chi_guo_xiang_qing_ye_url": self.base_url + p.xpath("./a/@href")[0],
                        "chi_gua_lie_biao_biao_ti": chi_guo_xiang_qing_nei_ro_item,
                    }
                    if i < len(chi_gua_xiang_qing_zhao_pian_lie_biao) - 1:
                        chi_gua_lie_biao_zi_dian["chi_gua_lie_biao_cover"] = chi_gua_xiang_qing_zhao_pian_lie_biao[i]
                    else:
                        # /media/sys/asdsadasd.png
                        chi_gua_lie_biao_zi_dian["chi_gua_lie_biao_cover"] = "/media/sys/asdsadasd.png"
                    chi_gua_lie_biao.append(chi_gua_lie_biao_zi_dian)

                chi_guo_xiang_qing_nei_ro += "\n".join(chi_gua_lie_biao_xiang_qing_nei_ro)

                continue

        # 获取m3u8播放链接
        m3u8_search = re.findall(r'"video":{"url":"(.*?)","pic":', html_text)
        if len(m3u8_search) == 0:
            m3u8_search = ""
        else:
            m3u8_search = str(m3u8_search[0]).replace("\\", "")
        m3u8_play_url = m3u8_search

        return {
            "chi_gua_lie_biao_biao_ti": chi_gua_lie_biao_biao_ti,
            "chi_gua_lie_biao_shang_xian_shi_jian": chi_gua_lie_biao_shang_xian_shi_jian,
            "chi_guo_xiang_qing_nei_ro": chi_guo_xiang_qing_nei_ro,
            "chi_gua_xiang_qing_zhao_pian_lie_biao": chi_gua_xiang_qing_zhao_pian_lie_biao,
            "m3u8_play_url": m3u8_play_url,
            "chi_gua_lie_biao": chi_gua_lie_biao,
            "shi_fo_wei_chi_gua_xiang_qing_lie_biao_he_ji": shi_fo_wei_chi_gua_xiang_qing_lie_biao_he_ji,
            "base_url": self.base_url
        }

    # 搜索内容
    def search_content(self, search_text):
        result = {
            "this_url": self.base_url + f"/search/{search_text}/"
        }
        response = {**self.get_gossip_list(result["this_url"]), **result}
        return response

    # 分页转换器
    def page_converter(self, page: int, this_page_url: str):
        """
        page: 你想到达的页面
        this_page_url: 你所在的页面url
        """
        this_page_url_split = this_page_url.split("/")
        new_url = self.base_url
        if this_page_url == new_url:
            # 完全等于基础url
            new_url = new_url + f"/page/{page}/"
        else:
            # 判断有没有page关键字
            if "page" in this_page_url:
                # 有page关键字
                new_url = this_page_url.replace(f"page/{this_page_url.split('page/')[-1]}", f"page/{page}/")
            elif "search" in this_page_url:
                # 判断搜索关键词的后面有没有跟着数字?
                search_url = this_page_url.split("/")
                if search_url[5] == "":
                    # 没有分页数
                    new_url = this_page_url + f"{page}/"
                else:
                    # 有分页数
                    new_url = this_page_url.replace(f"{search_url[5]}", f"{page}")
            elif len(this_page_url_split) >= 4:
                if not this_page_url_split[4].isdigit():
                    new_url = this_page_url + f"{page}/"
                    if this_page_url_split[5].isdigit():
                        new_url = this_page_url.replace(this_page_url_split[5], page)


            else:
                new_url = this_page_url + f"page/{page}/"

        return new_url

    # 获取最新图片域名
    def get_newest_image_domain(self) -> dict:
        # 请求首页数据
        image_domain = self.get_gossip_list(self.base_url)["chi_gua_lie_biao"][0]["chi_gua_lie_biao_cover"].split("/")[2]
        return {
            "image_domain": image_domain
        }
if __name__ == "__main__":
    piwivbdh5frz1 = PiwivbdH5frz1(True)
    piwivbdh5frz1.get_gossip_detail_data("https://BloodSpiderAV.vuexigs.top/archives/133430/")
    
 