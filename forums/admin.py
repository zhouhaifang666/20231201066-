from django.contrib import admin
from .models import Forum, ForumMember, ForumCategory, ForumCategoryRelation


@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    """贴吧管理"""
    
    list_display = ['name', 'creator', 'member_count', 'post_count', 'status', 'created_at']
    list_filter = ['status', 'is_public', 'join_need_approval', 'created_at']
    search_fields = ['name', 'description']
    filter_horizontal = ['moderators']
    readonly_fields = ['member_count', 'post_count', 'today_post_count']


@admin.register(ForumMember)
class ForumMemberAdmin(admin.ModelAdmin):
    """贴吧成员管理"""
    
    list_display = ['forum', 'user', 'role', 'joined_at', 'post_count']
    list_filter = ['role', 'joined_at']
    search_fields = ['forum__name', 'user__username']


@admin.register(ForumCategory)
class ForumCategoryAdmin(admin.ModelAdmin):
    """贴吧分类管理"""
    
    list_display = ['name', 'order']
    list_filter = ['order']
    search_fields = ['name']


@admin.register(ForumCategoryRelation)
class ForumCategoryRelationAdmin(admin.ModelAdmin):
    """贴吧分类关系管理"""
    
    list_display = ['forum', 'category']
    list_filter = ['category']
    search_fields = ['forum__name', 'category__name']