from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """自定义用户模型"""
    
    GENDER_CHOICES = [
        ('M', '男'),
        ('F', '女'),
        ('O', '其他'),
    ]
    
    nickname = models.CharField(max_length=50, verbose_name='昵称', blank=True)
    avatar = models.ImageField(upload_to='avatars/', verbose_name='头像', blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='性别', blank=True)
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name='手机号', blank=True)
    bio = models.TextField(verbose_name='个人简介', blank=True)
    
    # 社交信息
    wechat_openid = models.CharField(max_length=100, verbose_name='微信OpenID', blank=True)
    qq_openid = models.CharField(max_length=100, verbose_name='QQ OpenID', blank=True)
    
    # 统计信息
    post_count = models.PositiveIntegerField(verbose_name='发帖数', default=0)
    follower_count = models.PositiveIntegerField(verbose_name='粉丝数', default=0)
    following_count = models.PositiveIntegerField(verbose_name='关注数', default=0)
    
    # 时间戳
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
    
    def __str__(self):
        return self.nickname or self.username


class UserProfile(models.Model):
    """用户扩展信息"""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # 隐私设置
    show_email = models.BooleanField(verbose_name='显示邮箱', default=False)
    show_phone = models.BooleanField(verbose_name='显示手机号', default=False)
    
    # 偏好设置
    theme = models.CharField(max_length=20, verbose_name='主题', default='light')
    language = models.CharField(max_length=10, verbose_name='语言', default='zh')
    
    # 通知设置
    email_notifications = models.BooleanField(verbose_name='邮件通知', default=True)
    push_notifications = models.BooleanField(verbose_name='推送通知', default=True)
    
    class Meta:
        verbose_name = '用户配置'
        verbose_name_plural = '用户配置'
    
    def __str__(self):
        return f"{self.user.username} 的配置"