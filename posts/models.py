from django.db import models
from django.contrib.auth import get_user_model
from forums.models import Forum

User = get_user_model()


class Post(models.Model):
    """帖子模型"""
    
    STATUS_CHOICES = [
        ('published', '已发布'),
        ('draft', '草稿'),
        ('deleted', '已删除'),
        ('hidden', '隐藏'),
    ]
    
    TYPE_CHOICES = [
        ('normal', '普通帖'),
        ('sticky', '置顶帖'),
        ('announcement', '公告'),
        ('question', '问答'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, verbose_name='所属贴吧')
    
    # 帖子属性
    post_type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='normal', verbose_name='帖子类型')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published', verbose_name='状态')
    
    # 统计信息
    view_count = models.PositiveIntegerField(verbose_name='浏览数', default=0)
    reply_count = models.PositiveIntegerField(verbose_name='回复数', default=0)
    like_count = models.PositiveIntegerField(verbose_name='点赞数', default=0)
    collect_count = models.PositiveIntegerField(verbose_name='收藏数', default=0)
    
    # 时间戳
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    last_reply_at = models.DateTimeField(auto_now_add=True, verbose_name='最后回复时间')
    
    class Meta:
        verbose_name = '帖子'
        verbose_name_plural = '帖子'
        ordering = ['-last_reply_at', '-created_at']
        indexes = [
            models.Index(fields=['forum', 'status', 'post_type']),
            models.Index(fields=['author', 'created_at']),
        ]
    
    def __str__(self):
        return self.title


class Reply(models.Model):
    """回复模型"""
    
    STATUS_CHOICES = [
        ('published', '已发布'),
        ('deleted', '已删除'),
        ('hidden', '隐藏'),
    ]
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies', verbose_name='所属帖子')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    content = models.TextField(verbose_name='回复内容')
    
    # 回复属性
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published', verbose_name='状态')
    is_first_reply = models.BooleanField(default=False, verbose_name='是否首楼回复')
    
    # 引用回复
    parent_reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, 
                                   related_name='child_replies', verbose_name='父级回复')
    
    # 统计信息
    like_count = models.PositiveIntegerField(verbose_name='点赞数', default=0)
    
    # 时间戳
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        verbose_name = '回复'
        verbose_name_plural = '回复'
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['post', 'created_at']),
            models.Index(fields=['author', 'created_at']),
        ]
    
    def __str__(self):
        return f"{self.author.username} 的回复"


class PostLike(models.Model):
    """帖子点赞"""
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='帖子')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='点赞时间')
    
    class Meta:
        verbose_name = '帖子点赞'
        verbose_name_plural = '帖子点赞'
        unique_together = ['post', 'user']
    
    def __str__(self):
        return f"{self.user.username} 点赞了 {self.post.title}"


class ReplyLike(models.Model):
    """回复点赞"""
    
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE, verbose_name='回复')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='点赞时间')
    
    class Meta:
        verbose_name = '回复点赞'
        verbose_name_plural = '回复点赞'
        unique_together = ['reply', 'user']
    
    def __str__(self):
        return f"{self.user.username} 点赞了回复"


class PostCollection(models.Model):
    """帖子收藏"""
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='帖子')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='收藏时间')
    
    class Meta:
        verbose_name = '帖子收藏'
        verbose_name_plural = '帖子收藏'
        unique_together = ['post', 'user']
    
    def __str__(self):
        return f"{self.user.username} 收藏了 {self.post.title}"


class PostViewHistory(models.Model):
    """帖子浏览历史"""
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='帖子')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    viewed_at = models.DateTimeField(auto_now_add=True, verbose_name='浏览时间')
    
    class Meta:
        verbose_name = '帖子浏览历史'
        verbose_name_plural = '帖子浏览历史'
        ordering = ['-viewed_at']
    
    def __str__(self):
        return f"{self.user.username} 浏览了 {self.post.title}"