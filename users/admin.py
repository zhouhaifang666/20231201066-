from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """自定义用户管理界面"""
    
    list_display = ['username', 'nickname', 'email', 'gender', 'post_count', 'is_active', 'created_at']
    list_filter = ['gender', 'is_active', 'is_staff', 'created_at']
    search_fields = ['username', 'nickname', 'email']
    
    fieldsets = UserAdmin.fieldsets + (
        ('扩展信息', {
            'fields': ('nickname', 'avatar', 'gender', 'birthday', 'phone', 'bio')
        }),
        ('社交信息', {
            'fields': ('wechat_openid', 'qq_openid')
        }),
        ('统计信息', {
            'fields': ('post_count', 'follower_count', 'following_count')
        }),
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """用户配置管理"""
    
    list_display = ['user', 'show_email', 'show_phone', 'theme', 'language']
    list_filter = ['theme', 'language', 'show_email', 'show_phone']
    search_fields = ['user__username', 'user__nickname']