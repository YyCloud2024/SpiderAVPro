from django.shortcuts import render
import base64
from BloodSpiderModel.spider_tools.file_operate import FileOperate

file_operate = FileOperate()
# 全部线路
link_list = [file_operate.get_file_name(item) for item in file_operate.get_path_contents("BloodSpiderAPI/api", exclude_names=["__pycache__"], folders_only=True)]
config_result = {
    "link_list": link_list
}


# 自定义错误页
def custom_404(request, exception):
    return render(request, "pc/technical_404.html")

def custom_500(request):
    return render(request, "pc/technical_500.html")

# template
def template(request):
    return render(request, "pc/template.html")


# index
def index(request):
    result = {**config_result}
    return render(request, "pc/index.html", result)



# 线路首页
def link_index(request, link_name):
    # 判断link_name是否在link_list中
    if link_name not in link_list:
        return render(request, "pc/technical_404.html")
    result = {
        "link_name": link_name
    }
    return render(request, "pc/页面/首页.html", result)


# 播放页
def play_index(request, link_name, encode_base64_xiang_qing_ye_url):
    # 判断link_name是否在link_list中
    if link_name not in link_list:
        return render(request, "pc/technical_404.html")

    # 解密
    decode_base64_xiang_qing_ye_url = base64.b64decode(encode_base64_xiang_qing_ye_url).decode("utf-8")
    
    result = {
        "link_name": link_name,
        "encode_base64_xiang_qing_ye_url": encode_base64_xiang_qing_ye_url,
        "decode_base64_xiang_qing_ye_url": decode_base64_xiang_qing_ye_url
    }
    return render(request, "pc/页面/播放页.html", result)


# 我的收藏页
def my_collect(request):
    return render(request, "pc/页面/我的收藏页.html")

# 合集吃瓜列表页
def he_ji_chi_gua_lie_biao_ye(request, link_name, he_ji_ye_url):
    # 解密
    decode_base64_xiang_qing_ye_url = base64.b64decode(he_ji_ye_url).decode("utf-8")
    result = {
        "link_name": link_name,
        "he_ji_ye_url": he_ji_ye_url,
        "decode_base64_xiang_qing_ye_url": decode_base64_xiang_qing_ye_url
    }
    return render(request, "pc/页面/合集吃瓜列表页.html", result)