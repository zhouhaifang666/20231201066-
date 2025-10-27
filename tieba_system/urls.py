"""tieba_system URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/forums/', include('forums.urls')),
    path('api/posts/', include('posts.urls')),
    path('', include('forums.urls')),  # 主页面路由
]

# 开发环境下提供静态文件和媒体文件访问
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)