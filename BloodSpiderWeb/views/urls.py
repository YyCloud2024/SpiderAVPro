
from django.urls import path
from BloodSpiderWeb.views import all

urlpatterns = [
    path("", all.index),
    path("template/", all.template),
    path("index/", all.index),
    path("my_collect/", all.my_collect),
    path("link/<str:link_name>/", all.link_index),
    path("he_ji_lie_biao_ye/<str:link_name>/<str:he_ji_ye_url>/", all.he_ji_chi_gua_lie_biao_ye),
    path("play/<str:link_name>/<str:encode_base64_xiang_qing_ye_url>/", all.play_index),
]
