from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, UserProfile


class UserSerializer(serializers.ModelSerializer):
    """用户序列化器"""
    
    password = serializers.CharField(write_only=True, min_length=6)
    password_confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'nickname', 'password', 'password_confirm',
            'avatar', 'gender', 'birthday', 'phone', 'bio',
            'post_count', 'follower_count', 'following_count',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate(self, attrs):
        """验证密码确认"""
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("两次输入的密码不一致")
        return attrs
    
    def create(self, validated_data):
        """创建用户"""
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """用户配置序列化器"""
    
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = UserProfile
        fields = [
            'user', 'show_email', 'show_phone', 'theme', 'language',
            'email_notifications', 'push_notifications'
        ]


class LoginSerializer(serializers.Serializer):
    """登录序列化器"""
    
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        
        if username and password:
            return attrs
        raise serializers.ValidationError("用户名和密码不能为空")


class UserSimpleSerializer(serializers.ModelSerializer):
    """简化用户序列化器（用于列表显示）"""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'nickname', 'avatar']