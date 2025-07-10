
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.conf.urls import handler404, handler500
handler404 = 'BloodSpiderWeb.views.all.custom_404'  # 替换为你的视图路径
handler500 = 'BloodSpiderWeb.views.all.custom_500'  # 替换为你的视图路径
urlpatterns = [
    path("api/", include("BloodSpiderAPI.api.urls")),
    path("web/", include("BloodSpiderWeb.views.urls")),
    path("", include("BloodSpiderWeb.views.urls")),
]
# 添加媒体文件URL配置
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
