from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Forum(models.Model):
    """贴吧模型"""
    
    STATUS_CHOICES = [
        ('active', '活跃'),
        ('inactive', '不活跃'),
        ('closed', '已关闭'),
    ]
    
    name = models.CharField(max_length=100, verbose_name='贴吧名称', unique=True)
    description = models.TextField(verbose_name='贴吧描述', blank=True)
    avatar = models.ImageField(upload_to='forum_avatars/', verbose_name='贴吧头像', blank=True)
    banner = models.ImageField(upload_to='forum_banners/', verbose_name='贴吧横幅', blank=True)
    
    # 统计信息
    member_count = models.PositiveIntegerField(verbose_name='成员数', default=0)
    post_count = models.PositiveIntegerField(verbose_name='帖子数', default=0)
    today_post_count = models.PositiveIntegerField(verbose_name='今日发帖数', default=0)
    
    # 管理信息
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='创建者')
    moderators = models.ManyToManyField(User, related_name='moderated_forums', blank=True, verbose_name='版主')
    
    # 设置
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active', verbose_name='状态')
    is_public = models.BooleanField(default=True, verbose_name='是否公开')
    join_need_approval = models.BooleanField(default=False, verbose_name='加入需要审批')
    
    # 时间戳
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        verbose_name = '贴吧'
        verbose_name_plural = '贴吧'
        ordering = ['-post_count', '-created_at']
    
    def __str__(self):
        return self.name


class ForumMember(models.Model):
    """贴吧成员"""
    
    ROLE_CHOICES = [
        ('member', '普通成员'),
        ('moderator', '版主'),
        ('admin', '管理员'),
    ]
    
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, verbose_name='贴吧')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member', verbose_name='角色')
    
    # 成员信息
    joined_at = models.DateTimeField(auto_now_add=True, verbose_name='加入时间')
    last_visit = models.DateTimeField(auto_now=True, verbose_name='最后访问时间')
    post_count = models.PositiveIntegerField(verbose_name='发帖数', default=0)
    
    class Meta:
        verbose_name = '贴吧成员'
        verbose_name_plural = '贴吧成员'
        unique_together = ['forum', 'user']
        ordering = ['-joined_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.forum.name}"


class ForumCategory(models.Model):
    """贴吧分类"""
    
    name = models.CharField(max_length=50, verbose_name='分类名称')
    description = models.TextField(verbose_name='分类描述', blank=True)
    order = models.PositiveIntegerField(verbose_name='排序', default=0)
    
    class Meta:
        verbose_name = '贴吧分类'
        verbose_name_plural = '贴吧分类'
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name


class ForumCategoryRelation(models.Model):
    """贴吧与分类关系"""
    
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, verbose_name='贴吧')
    category = models.ForeignKey(ForumCategory, on_delete=models.CASCADE, verbose_name='分类')
    
    class Meta:
        verbose_name = '贴吧分类关系'
        verbose_name_plural = '贴吧分类关系'
        unique_together = ['forum', 'category']
    
    def __str__(self):
        return f"{self.forum.name} - {self.category.name}"