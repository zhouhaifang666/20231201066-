from django.urls import path
from . import views

urlpatterns = [
    # 认证相关
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    
    # 用户信息
    path('current/', views.current_user, name='current_user'),
    path('profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('me/', views.UserDetailView.as_view(), name='user_detail'),
]