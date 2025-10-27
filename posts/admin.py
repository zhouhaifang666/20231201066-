from django.contrib import admin
from .models import Post, Reply, PostLike, ReplyLike, PostCollection, PostViewHistory


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """帖子管理"""
    
    list_display = ['title', 'author', 'forum', 'post_type', 'status', 'view_count', 'reply_count', 'created_at']
    list_filter = ['post_type', 'status', 'forum', 'created_at']
    search_fields = ['title', 'content', 'author__username']
    readonly_fields = ['view_count', 'reply_count', 'like_count', 'collect_count']


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    """回复管理"""
    
    list_display = ['post', 'author', 'status', 'like_count', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['content', 'author__username', 'post__title']
    readonly_fields = ['like_count']


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    """帖子点赞管理"""
    
    list_display = ['post', 'user', 'created_at']
    list_filter = ['created_at']
    search_fields = ['post__title', 'user__username']


@admin.register(ReplyLike)
class ReplyLikeAdmin(admin.ModelAdmin):
    """回复点赞管理"""
    
    list_display = ['reply', 'user', 'created_at']
    list_filter = ['created_at']
    search_fields = ['reply__content', 'user__username']


@admin.register(PostCollection)
class PostCollectionAdmin(admin.ModelAdmin):
    """帖子收藏管理"""
    
    list_display = ['post', 'user', 'created_at']
    list_filter = ['created_at']
    search_fields = ['post__title', 'user__username']


@admin.register(PostViewHistory)
class PostViewHistoryAdmin(admin.ModelAdmin):
    """帖子浏览历史管理"""
    
    list_display = ['post', 'user', 'viewed_at']
    list_filter = ['viewed_at']
    search_fields = ['post__title', 'user__username']