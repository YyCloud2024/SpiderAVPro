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
            # result = {
            #     "chi_gua_lie_biao_biao_ti": "萝莉猎手唐伯虎合集连载中🔥🔥🔥已更新49部",
            #     "chi_gua_lie_biao_shang_xian_shi_jian": "2025 年 06 月 30 日",
            #     "chi_guo_xiang_qing_nei_ro": "排名不分先后\n推特博主唐伯虎  调教白色长筒袜学生妹  跳蛋玩弄白虎逼  大屌插进子宫 呻吟娇喘 \n91大神唐伯虎 白色条纹长袜的淫荡小母狗 被主人大屌一插到底 爽的小母狗骚浪淫叫\n91大神唐伯虎  猛操白袜子淫奴学生妹  大粗屌直插深处   鲜嫩白虎蜜穴紧致吸吮\n萝莉少女大神唐伯虎 白嫩少女观音坐莲  娇嫩白虎美穴吞吐大鸡巴的样子好淫荡\n萝莉杀手唐伯虎 大粗屌爆肏开档JK制服学妹 绝妙快感爽到抖臀 爸爸到底了好爽\n嫩妹杀手唐伯虎 调教大一白虎嫩学妹 加极品幼师 二合一分类拼接合集 \n唐伯虎专操嫩逼 极品白丝萝莉被大粗屌深宫搅动  蜜臀痉挛中\n唐伯虎系列之 调教高中生小母狗 三合一 个个都是高颜值学生妹 一个比一个嫩 还有校服系列 \n唐伯虎精选 后入大二嫩母狗 隔着透明窗户操逼那一段太有感觉了 爽得妹子直抓奶浪叫呻吟\n推特大神 唐伯虎 约操大长腿校花学妹束缚调教 大长美腿配黑色过膝袜 在大鸡巴下变成淫荡的小母狗\n超推荐大神唐伯虎  小母狗撅着屁股挨调教  超大道具插入紧致白虎嫩穴\n国产大神 唐伯虎 未流出珍藏版本 后入爆操COS女仆小麋鹿嫩少女 白浆四射 \n 萝莉猎手 40万粉丝国产大神「唐伯虎」OF私拍 黑色丝袜死库水小母狗接受性爱调教\n 唐伯虎在约操白虎嫩学妹 没次都是白虎 没次女主都不一样 真的羡慕\n 大神唐伯虎约操白虎嫩学妹 OF未流出高清版 大屌专操粉穴 粉嫩小肉洞都要被撑爆了\n 唐伯虎约操00后高三母狗 同学老师眼中的乖乖女私下超级反差 扒开大腿插到子宫\n 嫩穴收割机 大神唐伯虎 爆操高三校服白虎学妹 扒开玉臀抽插 高清源码\n 嫩穴收割机 大神唐伯虎 专攻美少女 00后高三学妹超清源码稀缺 1-3\n 91唐伯虎 酒店约操身穿篮球服点极品幼师妹子 无套顶操内射\n推特博主唐伯虎  穿上网衣短袜的学生妹小女友被调教  大屌骑乘位爆操白虎骚穴\n推特91大神唐伯虎 调教00后极品幼师 女上位全自动包裹大屌 快速抽插 享受高潮的快感\n推特博主唐伯虎 约操35岁风骚人妻  肥嫩的鲍鱼被大屌插入 淫荡的叫声表示完全被征服\n萝莉杀手唐伯虎 再操穿小棉袜学生妹 女上位的姿势一插到底  干净的屁眼看着好诱人\n萝莉约炮大神 唐伯虎  爆操黑丝连体衣学妹  极品白虎蜜桃臀疯狂无套榨汁\n约炮萝莉大神  91唐伯虎约操深圳校服白虎学生妹  小穴十分紧致粉嫩 包裹一整根大肉棒\n约炮萝莉大神 91唐伯虎约操深圳ol职业装嫩妹 享受大鸡巴抽插的快乐\n萝莉约炮杀手 91唐伯虎狂操透明衬衫戴牙套萝莉  怼脸怼逼拍摄特写 \n萝莉猎手91大神唐伯虎 道具调教网瘾少女 跳蛋塞逼里 高清实拍抽插动作\n萝莉猎手 91唐伯虎大屌深插清纯学生妹 脖子上戴项圈 多种姿势遭受猛烈撞击\n萝莉猎手91唐伯虎 让妹子先吃跳跳糖再进行口交  跳蛋塞逼里玩出水再插入大屌 太会玩了\n萝莉猎手 91大神唐伯虎爆操大奶新女主  撕开丝袜露出嫩逼 等待大屌的插入\n约炮萝莉唐伯虎 调教玩弄深圳高三学妹 早期经典作品 \n91大神唐伯虎 专操萝莉 身穿白色情趣内衣体验性爱 射精后也舍不得把鸡巴拔出来\n91大神唐伯虎 再约高三学妹很害羞 先温柔的口交服务 再操大屁股小萝莉 逼嫩逼毛多\n萝莉杀手唐伯虎 约操纯天然白虎学生妹  逼里全是水 被操的哗哗响\n91大神唐伯虎 跳蛋调教开档黑丝高三学妹 用舌头包裹主人的大鸡巴 \n专约少女萝莉大神唐伯虎 大屌后入调教高三学妹 干的嗷嗷叫 小骚逼都被塞满了\n萝莉杀手唐伯虎 美鲍小嫩穴被塞入跳蛋调教 屁股撅起来干到噗嗤噗嗤响\n萝莉学生妹杀手唐伯虎  逼里塞跳蛋 用震动棒玩弄阴蒂  无套多姿势爆操 射精液到肚子上\n萝莉学生妹猎手唐伯虎 酒店约操新女主 臀大逼嫩 全程女上位榨精 \n91约炮大神唐伯虎 约操01年幼师 打桩机爆插蜜桃臀 全身红点 是水痘还是生化母体\n91大神唐伯虎花式操嫩妹第一部 这开档肉丝完美腰臀比 屁股浑圆饱满太美了 \n91大神唐伯虎花式操嫩妹第二部 妹子的小穴十分紧致 倒入润滑液插入大屌 妹子大喊不行\n91大神唐伯虎剃毛作品上部 跳蛋调教无毛的嫩逼 享受萝莉学生妹的温柔口交服务\n91大神唐伯虎剃毛作品下部 倒入润滑用就直接插入巨根 快速的抽动忍不住内射 \n91唐伯虎 无套中出短发校服白袜学生妹 大屌撑开的小嫩逼  有近距离视角很赞\n推特91大神唐伯虎 高难度新姿势爆操00后学妹 做爱一半感觉不爽还把套子摘掉了 最后无套内射\n唐伯虎探花精选 极品白嫩大长腿学生妹被无套爆操内射 妹子的身材是真的顶！\n大神唐伯虎约炮只约小萝莉 穿着死库水的小萝莉 撅起屁股等着主人的大鸡巴插入嫩逼！\n",
            #     "chi_gua_xiang_qing_zhao_pian_lie_biao": [
            #         "https://pic.duofyi.cn/upload_01/xiao/20240802/2024080223465717582.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240801/2024080122451829099.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240730/2024073020501763880.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240725/2024072519523054805.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240724/2024072411353821978.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240723/2024072322125180821.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240719/2024071916164545666.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240718/2024071822161541338.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240717/2024071722163761732.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240715/2024071518254721819.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240710/2024071011134556204.jpeg",
            #         "https://pic.duofyi.cn/upload/xiao/20240608/2024060814504297545.jpeg",
            #         "https://pic.duofyi.cn/upload/xiao/20240429/2024042920090957187.jpeg",
            #         "https://pic.duofyi.cn/upload/xiao/20240418/2024041818144370315.jpeg",
            #         "https://pic.duofyi.cn/upload/xiao/20240417/2024041720270845564.jpeg",
            #         "https://pic.duofyi.cn/upload/xiao/20231214/2023121418255682570.jpeg",
            #         "https://pic.duofyi.cn/upload/xiao/20231209/2023120915040921231.jpeg",
            #         "https://pic.duofyi.cn/upload/xiao/20231207/2023120717245752194.jpeg",
            #         "https://pic.duofyi.cn/upload/xiao/20231206/2023120612342333389.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240805/2024080511325560325.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240812/2024081222240263693.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240813/2024081319460291966.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240815/2024081522084859401.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240816/2024081622311015338.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240820/2024082021104071343.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240821/2024082121010425256.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240822/2024082219552764684.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240823/2024082320524016071.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240824/2024082417183344321.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240826/2024082623154834512.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240829/2024082920051455995.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240830/2024083022454681256.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240831/2024083115265622752.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240901/2024090120224437692.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240902/2024090220412573505.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240904/2024090422540510755.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240905/2024090521032210547.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240909/2024090921393124942.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240910/2024091022123186406.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240911/2024091118354252076.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240912/2024091222063824412.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240913/2024091321162190066.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240913/2024091321395921430.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240919/2024091922015242782.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240919/2024091922015242782.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20240924/2024092422021394473.jpeg",
            #         "https://pic.duofyi.cn/upload_01/xiao/20241004/2024100422405512292.jpeg",
            #         "https://pic.duofyi.cn/upload_01/position/20250330/2025033016225562448.jpg",
            #         "https://pic.duofyi.cn/upload_01/position/20250519/2025051916580373866.jpg"
            #     ],
            #     "m3u8_play_url": "",
            #     "chi_gua_lie_biao": [
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/81403/",
            #             "chi_gua_lie_biao_biao_ti": "推特博主唐伯虎  调教白色长筒袜学生妹  跳蛋玩弄白虎逼  大屌插进子宫 呻吟娇喘 ",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240802/2024080223465717582.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/81069/",
            #             "chi_gua_lie_biao_biao_ti": "91大神唐伯虎 白色条纹长袜的淫荡小母狗 被主人大屌一插到底 爽的小母狗骚浪淫叫",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240801/2024080122451829099.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/80466/",
            #             "chi_gua_lie_biao_biao_ti": "91大神唐伯虎  猛操白袜子淫奴学生妹  大粗屌直插深处   鲜嫩白虎蜜穴紧致吸吮",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240730/2024073020501763880.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/79204/",
            #             "chi_gua_lie_biao_biao_ti": "萝莉少女大神唐伯虎 白嫩少女观音坐莲  娇嫩白虎美穴吞吐大鸡巴的样子好淫荡",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240725/2024072519523054805.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/78658/",
            #             "chi_gua_lie_biao_biao_ti": "萝莉杀手唐伯虎 大粗屌爆肏开档JK制服学妹 绝妙快感爽到抖臀 爸爸到底了好爽",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240724/2024072411353821978.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/78614/",
            #             "chi_gua_lie_biao_biao_ti": "嫩妹杀手唐伯虎 调教大一白虎嫩学妹 加极品幼师 二合一分类拼接合集 ",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240723/2024072322125180821.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/77220/",
            #             "chi_gua_lie_biao_biao_ti": "唐伯虎专操嫩逼 极品白丝萝莉被大粗屌深宫搅动  蜜臀痉挛中",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240719/2024071916164545666.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/77062/",
            #             "chi_gua_lie_biao_biao_ti": "唐伯虎系列之 调教高中生小母狗 三合一 个个都是高颜值学生妹 一个比一个嫩 还有校服系列 ",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240718/2024071822161541338.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/76804/",
            #             "chi_gua_lie_biao_biao_ti": "唐伯虎精选 后入大二嫩母狗 隔着透明窗户操逼那一段太有感觉了 爽得妹子直抓奶浪叫呻吟",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240717/2024071722163761732.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/76211/",
            #             "chi_gua_lie_biao_biao_ti": "推特大神 唐伯虎 约操大长腿校花学妹束缚调教 大长美腿配黑色过膝袜 在大鸡巴下变成淫荡的小母狗",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240715/2024071518254721819.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/74330/",
            #             "chi_gua_lie_biao_biao_ti": "超推荐大神唐伯虎  小母狗撅着屁股挨调教  超大道具插入紧致白虎嫩穴",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240710/2024071011134556204.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/64694/",
            #             "chi_gua_lie_biao_biao_ti": "国产大神 唐伯虎 未流出珍藏版本 后入爆操COS女仆小麋鹿嫩少女 白浆四射 ",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload/xiao/20240608/2024060814504297545.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/55929/",
            #             "chi_gua_lie_biao_biao_ti": " 萝莉猎手 40万粉丝国产大神「唐伯虎」OF私拍 黑色丝袜死库水小母狗接受性爱调教",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload/xiao/20240429/2024042920090957187.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/54080/",
            #             "chi_gua_lie_biao_biao_ti": " 唐伯虎在约操白虎嫩学妹 没次都是白虎 没次女主都不一样 真的羡慕",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload/xiao/20240418/2024041818144370315.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/53889/",
            #             "chi_gua_lie_biao_biao_ti": " 大神唐伯虎约操白虎嫩学妹 OF未流出高清版 大屌专操粉穴 粉嫩小肉洞都要被撑爆了",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload/xiao/20240417/2024041720270845564.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/37151/",
            #             "chi_gua_lie_biao_biao_ti": " 唐伯虎约操00后高三母狗 同学老师眼中的乖乖女私下超级反差 扒开大腿插到子宫",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload/xiao/20231214/2023121418255682570.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/36528/",
            #             "chi_gua_lie_biao_biao_ti": " 嫩穴收割机 大神唐伯虎 爆操高三校服白虎学妹 扒开玉臀抽插 高清源码",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload/xiao/20231209/2023120915040921231.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/36285/",
            #             "chi_gua_lie_biao_biao_ti": " 嫩穴收割机 大神唐伯虎 专攻美少女 00后高三学妹超清源码稀缺 1-3",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload/xiao/20231207/2023120717245752194.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/36080/",
            #             "chi_gua_lie_biao_biao_ti": " 91唐伯虎 酒店约操身穿篮球服点极品幼师妹子 无套顶操内射",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload/xiao/20231206/2023120612342333389.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/81866/",
            #             "chi_gua_lie_biao_biao_ti": "推特博主唐伯虎  穿上网衣短袜的学生妹小女友被调教  大屌骑乘位爆操白虎骚穴",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240805/2024080511325560325.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/83845/",
            #             "chi_gua_lie_biao_biao_ti": "推特91大神唐伯虎 调教00后极品幼师 女上位全自动包裹大屌 快速抽插 享受高潮的快感",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240812/2024081222240263693.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/84119/",
            #             "chi_gua_lie_biao_biao_ti": "推特博主唐伯虎 约操35岁风骚人妻  肥嫩的鲍鱼被大屌插入 淫荡的叫声表示完全被征服",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240813/2024081319460291966.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/84782/",
            #             "chi_gua_lie_biao_biao_ti": "萝莉杀手唐伯虎 再操穿小棉袜学生妹 女上位的姿势一插到底  干净的屁眼看着好诱人",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240815/2024081522084859401.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/85047/",
            #             "chi_gua_lie_biao_biao_ti": "萝莉约炮大神 唐伯虎  爆操黑丝连体衣学妹  极品白虎蜜桃臀疯狂无套榨汁",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240816/2024081622311015338.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/85868/",
            #             "chi_gua_lie_biao_biao_ti": "约炮萝莉大神  91唐伯虎约操深圳校服白虎学生妹  小穴十分紧致粉嫩 包裹一整根大肉棒",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240820/2024082021104071343.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/86153/",
            #             "chi_gua_lie_biao_biao_ti": "约炮萝莉大神 91唐伯虎约操深圳ol职业装嫩妹 享受大鸡巴抽插的快乐",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240821/2024082121010425256.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/86411/",
            #             "chi_gua_lie_biao_biao_ti": "萝莉约炮杀手 91唐伯虎狂操透明衬衫戴牙套萝莉  怼脸怼逼拍摄特写 ",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240822/2024082219552764684.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/86729/",
            #             "chi_gua_lie_biao_biao_ti": "萝莉猎手91大神唐伯虎 道具调教网瘾少女 跳蛋塞逼里 高清实拍抽插动作",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240823/2024082320524016071.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/87003/",
            #             "chi_gua_lie_biao_biao_ti": "萝莉猎手 91唐伯虎大屌深插清纯学生妹 脖子上戴项圈 多种姿势遭受猛烈撞击",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240824/2024082417183344321.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/87495/",
            #             "chi_gua_lie_biao_biao_ti": "萝莉猎手91唐伯虎 让妹子先吃跳跳糖再进行口交  跳蛋塞逼里玩出水再插入大屌 太会玩了",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240826/2024082623154834512.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/88136/",
            #             "chi_gua_lie_biao_biao_ti": "萝莉猎手 91大神唐伯虎爆操大奶新女主  撕开丝袜露出嫩逼 等待大屌的插入",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240829/2024082920051455995.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/88337/",
            #             "chi_gua_lie_biao_biao_ti": "约炮萝莉唐伯虎 调教玩弄深圳高三学妹 早期经典作品 ",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240830/2024083022454681256.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/88420/",
            #             "chi_gua_lie_biao_biao_ti": "91大神唐伯虎 专操萝莉 身穿白色情趣内衣体验性爱 射精后也舍不得把鸡巴拔出来",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240831/2024083115265622752.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/88565/",
            #             "chi_gua_lie_biao_biao_ti": "91大神唐伯虎 再约高三学妹很害羞 先温柔的口交服务 再操大屁股小萝莉 逼嫩逼毛多",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240901/2024090120224437692.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/88794/",
            #             "chi_gua_lie_biao_biao_ti": "萝莉杀手唐伯虎 约操纯天然白虎学生妹  逼里全是水 被操的哗哗响",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240902/2024090220412573505.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/89174/",
            #             "chi_gua_lie_biao_biao_ti": "91大神唐伯虎 跳蛋调教开档黑丝高三学妹 用舌头包裹主人的大鸡巴 ",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240904/2024090422540510755.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/89393/",
            #             "chi_gua_lie_biao_biao_ti": "专约少女萝莉大神唐伯虎 大屌后入调教高三学妹 干的嗷嗷叫 小骚逼都被塞满了",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240905/2024090521032210547.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/90100/",
            #             "chi_gua_lie_biao_biao_ti": "萝莉杀手唐伯虎 美鲍小嫩穴被塞入跳蛋调教 屁股撅起来干到噗嗤噗嗤响",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240909/2024090921393124942.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/90321/",
            #             "chi_gua_lie_biao_biao_ti": "萝莉学生妹杀手唐伯虎  逼里塞跳蛋 用震动棒玩弄阴蒂  无套多姿势爆操 射精液到肚子上",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240910/2024091022123186406.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/90472/",
            #             "chi_gua_lie_biao_biao_ti": "萝莉学生妹猎手唐伯虎 酒店约操新女主 臀大逼嫩 全程女上位榨精 ",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240911/2024091118354252076.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/90769/",
            #             "chi_gua_lie_biao_biao_ti": "91约炮大神唐伯虎 约操01年幼师 打桩机爆插蜜桃臀 全身红点 是水痘还是生化母体",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240912/2024091222063824412.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/90950/",
            #             "chi_gua_lie_biao_biao_ti": "91大神唐伯虎花式操嫩妹第一部 这开档肉丝完美腰臀比 屁股浑圆饱满太美了 ",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240913/2024091321162190066.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/90958/",
            #             "chi_gua_lie_biao_biao_ti": "91大神唐伯虎花式操嫩妹第二部 妹子的小穴十分紧致 倒入润滑液插入大屌 妹子大喊不行",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240913/2024091321395921430.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/91814/",
            #             "chi_gua_lie_biao_biao_ti": "91大神唐伯虎剃毛作品上部 跳蛋调教无毛的嫩逼 享受萝莉学生妹的温柔口交服务",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240919/2024091922015242782.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/92556/",
            #             "chi_gua_lie_biao_biao_ti": "91大神唐伯虎剃毛作品下部 倒入润滑用就直接插入巨根 快速的抽动忍不住内射 ",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240919/2024091922015242782.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/92795/",
            #             "chi_gua_lie_biao_biao_ti": "91唐伯虎 无套中出短发校服白袜学生妹 大屌撑开的小嫩逼  有近距离视角很赞",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20240924/2024092422021394473.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/94814/",
            #             "chi_gua_lie_biao_biao_ti": "推特91大神唐伯虎 高难度新姿势爆操00后学妹 做爱一半感觉不爽还把套子摘掉了 最后无套内射",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/xiao/20241004/2024100422405512292.jpeg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/118885/",
            #             "chi_gua_lie_biao_biao_ti": "唐伯虎探花精选 极品白嫩大长腿学生妹被无套爆操内射 妹子的身材是真的顶！",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/position/20250330/2025033016225562448.jpg"
            #         },
            #         {
            #             "chi_guo_xiang_qing_ye_url": "https://ah.qofscsjb.me/archives/125786/",
            #             "chi_gua_lie_biao_biao_ti": "大神唐伯虎约炮只约小萝莉 穿着死库水的小萝莉 撅起屁股等着主人的大鸡巴插入嫩逼！",
            #             "chi_gua_lie_biao_cover": "https://pic.duofyi.cn/upload_01/position/20250519/2025051916580373866.jpg"
            #         }
            #     ],
            #     "shi_fo_wei_chi_gua_xiang_qing_lie_biao_he_ji": true,
            #     "base_url": "https://ah.qofscsjb.me"
            # }
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


