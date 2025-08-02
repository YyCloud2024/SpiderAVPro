import time
from BloodSpiderModel.DjangoResponseTool.response_dict import response_dict

from av_spider.com_piwivbd_h5frz1.com_piwivbd_h5frz1_01 import PiwivbdH5frz1
from SpiderAvPro import settings
spider = PiwivbdH5frz1(settings.DEBUG)

def get_classifications(request):
    """获取吃瓜总分类"""
    if request.method == "GET":
        try:
            classifications = spider.get_gossip_total_categories_cached()
            return response_dict(code=0, message="获取分类成功", data=classifications)
        except Exception as e:
            return response_dict(code=1, message=f"获取分类失败: {str(e)}", data=None)
    else:
        return response_dict(code=1, message="请求方式错误", data=None)


# 获取最新的图片域名
def get_newest_image_domain(request):
    return response_dict(data=spider.get_newest_image_domain())

def get_gossip_list(request):
    """获取吃瓜列表"""
    if request.method == "GET":
        try:
            gossip_list_url = request.GET.get('url')
            result = spider.get_gossip_list(gossip_list_url)
            # result = {
            #     "chi_gua_lie_biao": [
            #         {
            #             "chi_gua_lie_biao_biao_ti": "南京红姐事件全网最全版 约炮千位猛男 三年拍摄视频1000部 扮演萝莉TS吃遍直男肌肉帅哥",
            #             "chi_guo_xiang_qing_ye_url": "https://d1rr44zdbwhoo7.fklbndy.top/archives/131646/",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20250703/2025070322104049380.jpeg"
            #         },
            #         {
            #             "chi_gua_lie_biao_biao_ti": "南京阿红事件 TS伪娘红姐 大家都要的牛奶哥来了 过来还不忘给老嫂子带箱牛奶补身子",
            #             "chi_guo_xiang_qing_ye_url": "https://d1rr44zdbwhoo7.fklbndy.top/archives/131979/",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20250708/2025070800280337735.jpeg"
            #         },
            #         {
            #             "chi_gua_lie_biao_biao_ti": "抖音200万粉丝COS网红 瑶兔叽 男女通吃患有性瘾 与金主一晚高潮30次 录音视频聊天记录曝光",
            #             "chi_guo_xiang_qing_ye_url": "https://d1rr44zdbwhoo7.fklbndy.top/archives/131545/",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20250703/2025070318462280248.jpeg"
            #         },
            #         {
            #             "chi_gua_lie_biao_biao_ti": "法修散打变装合集 抖音风极品嫩妹大尺度擦边热舞 性感装扮下的视觉盛宴一次看个够",
            #             "chi_guo_xiang_qing_ye_url": "https://d1rr44zdbwhoo7.fklbndy.top/archives/131325/",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20250702/2025070218360463222.jpeg"
            #         },
            #         {
            #             "chi_gua_lie_biao_biao_ti": "抖音百万网红 静静爱吃糖 福利姬合集 土豪定制大尺度视频 狂野自慰妥妥精液收集者",
            #             "chi_guo_xiang_qing_ye_url": "https://d1rr44zdbwhoo7.fklbndy.top/archives/131098/",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20250701/2025070117054832266.jpeg"
            #         },
            #         {
            #             "chi_gua_lie_biao_biao_ti": "抖音200万粉网红 夏蓝 私密视频流出 欧美风女神大尺度口交 金主爸爸狂野后入",
            #             "chi_guo_xiang_qing_ye_url": "https://d1rr44zdbwhoo7.fklbndy.top/archives/131113/",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20250701/2025070118231469446.jpeg"
            #         },
            #         {
            #             "chi_gua_lie_biao_biao_ti": "南京阿红 盘点那些年睡过红姐的男人大头照曝光 集美们快来认领你心目中的小帅男神",
            #             "chi_guo_xiang_qing_ye_url": "https://d1rr44zdbwhoo7.fklbndy.top/archives/131934/",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20250707/2025070720384226569.jpeg"
            #         },
            #         {
            #             "chi_gua_lie_biao_biao_ti": "南京阿红约炮视频全网最全合集来了 3年内1000部视频 持续更新中！",
            #             "chi_guo_xiang_qing_ye_url": "https://d1rr44zdbwhoo7.fklbndy.top/archives/131840/",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20250707/2025070702454747839.jpeg"
            #         },
            #         {
            #             "chi_gua_lie_biao_biao_ti": "推特人妻 秦嘉倪 秦嘉妮 luki66887 与老公旅游性爱合集 超白肥臀骑乘后入暴操",
            #             "chi_guo_xiang_qing_ye_url": "https://d1rr44zdbwhoo7.fklbndy.top/archives/131802/",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20250705/2025070512571715604.jpeg"
            #         },
            #         {
            #             "chi_gua_lie_biao_biao_ti": "抖音人气网红 小水一号 泳池边比基尼视频流出 性感摆拍反差撩人 泪眼迷离楚楚可怜",
            #             "chi_guo_xiang_qing_ye_url": "https://d1rr44zdbwhoo7.fklbndy.top/archives/131789/",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20250704/2025070419355044085.jpeg"
            #         },
            #         {
            #             "chi_gua_lie_biao_biao_ti": "抖音365万粉 无敌暴龙战神 肖雅婷 性爱视频流出 清纯萝莉变狂野尤物 反差感震碎三观",
            #             "chi_guo_xiang_qing_ye_url": "https://d1rr44zdbwhoo7.fklbndy.top/archives/131650/",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20250704/2025070412385451889.jpeg"
            #         },
            #         {
            #             "chi_gua_lie_biao_biao_ti": "宜家女主户外露出系列4 高端设备耳音颅内高潮简称ASMR销魂自慰 不一样的视觉听觉刺激！",
            #             "chi_guo_xiang_qing_ye_url": "https://d1rr44zdbwhoo7.fklbndy.top/archives/132052/",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20250708/2025070818281220614.jpeg"
            #         }
            #     ],
            #     "chi_gua_lie_biao_fe_ye": {
            #         "chi_gua_lie_biao_fe_ye_dang_qian_ye": "1",
            #         "chi_gua_lie_biao_fe_ye_zo_fe_ye": "880"
            #     },
            #     "base_url": "https://d1rr44zdbwhoo7.fklbndy.top",
            #     "blog_title": "蜘蛛爆料网 - 吃瓜爆料聚集地"
            # }
            # time.sleep(500)
            return response_dict(code=0, message="获取吃瓜列表成功", data=result)
        except Exception as e:
            return response_dict(code=1, message=f"获取吃瓜列表失败: {str(e)}", data=None)
    else:
        return response_dict(code=1, message="请求方式错误", data=None)


def get_gossip_detail(request):
    """获取吃瓜详情内容数据"""
    if request.method == "GET":
        try:
            detail_url = request.GET.get('url')
            if not detail_url:
                return response_dict(code=1, message="详情URL不能为空", data=None)
            
            result = spider.get_gossip_detail_data(detail_url)
            return response_dict(code=0, message="获取吃瓜详情成功", data=result)
        except Exception as e:
            return response_dict(code=1, message=f"获取吃瓜详情失败: {str(e)}", data=None)
    else:
        return response_dict(code=1, message="请求方式错误", data=None)


def search_content(request):
    """搜索内容"""
    if request.method == "GET":
        try:
            search_text = request.GET.get('keyword', '')
            if not search_text:
                return response_dict(code=1, message="搜索关键词不能为空", data=None)
            
            result = spider.search_content(search_text)
            # result = {
            #     "chi_gua_lie_biao": [
            #         {
            #             "chi_gua_lie_biao_biao_ti": "炸裂！又一起师生不伦恋 某职高女老师和学生在学校公园直接开操 周围人走来走去毫不在意",
            #             "chi_guo_xiang_qing_ye_url": "https://accept.fklbndy.top/archives/45565/",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload/xiao/20240221/2024022117380626465.jpeg"
            #         }
            #     ],
            #     "chi_gua_lie_biao_fe_ye": {
            #         "chi_gua_lie_biao_fe_ye_dang_qian_ye": "1",
            #         "chi_gua_lie_biao_fe_ye_zo_fe_ye": "1"
            #     },
            #     "base_url": "https://d1rr44zdbwhoo7.fklbndy.top",
            #     "this_url": "https://d1rr44zdbwhoo7.fklbndy.top/search/初中生/"
            # }
            return response_dict(code=0, message="搜索成功", data=result)
        except Exception as e:
            return response_dict(code=1, message=f"搜索失败: {str(e)}", data=None)
    else:
        return response_dict(code=1, message="请求方式错误", data=None)


def page_converter(request):
    """分页转换器"""
    if request.method == "GET":
        try:
            page = request.GET.get('page', '1')
            this_page_url = request.GET.get('this_page_url')
            if not this_page_url:
                return response_dict(code=1, message="当前页面URL不能为空", data=None)
            
            result = spider.page_converter(page, this_page_url)
            return response_dict(code=0, message="转换成功", data=result)
        except Exception as e:
            return response_dict(code=1, message=f"转换失败: {str(e)}", data=None)
    else:
        return response_dict(code=1, message="请求方式错误", data=None)


