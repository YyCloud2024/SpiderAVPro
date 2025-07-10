from django.urls import path, include
from . import com_piwivbd_h5frz1_01

urlpatterns = [
    # 获取吃瓜总分类
    path('classifications/', com_piwivbd_h5frz1_01.get_classifications, name='get_classifications'),
    
    # 获取吃瓜列表
    path('gossip-list/', com_piwivbd_h5frz1_01.get_gossip_list, name='get_gossip_list'),
    
    # 获取吃瓜详情内容数据
    path('gossip-detail/', com_piwivbd_h5frz1_01.get_gossip_detail, name='get_gossip_detail'),
    
    # 搜索内容
    path('search/', com_piwivbd_h5frz1_01.search_content, name='search_content'),

    # 分页转换器
    path('page-converter/', com_piwivbd_h5frz1_01.page_converter, name='page_converter'),
]
