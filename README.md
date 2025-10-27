# 贴吧系统 - Django版本

基于Django框架开发的现代化贴吧系统，支持用户注册登录、贴吧管理、发帖回帖等功能。

## 功能特性

### 用户系统
- 用户注册、登录、登出
- 个人信息管理
- 头像上传
- 社交账号绑定

### 贴吧管理
- 贴吧创建和管理
- 贴吧分类
- 成员管理
- 版主权限

### 帖子系统
- 发帖、回帖
- 帖子点赞、收藏
- 帖子浏览历史
- 帖子类型（普通、置顶、公告等）

### 管理后台
- 完整的Django Admin后台
- 用户管理
- 贴吧管理
- 内容审核

## 技术栈

- **后端**: Django 4.2.7 + Django REST Framework
- **数据库**: SQLite (开发) / MySQL (生产)
- **缓存**: Redis
- **任务队列**: Celery
- **文件存储**: 本地存储 / 云存储

## 项目结构

```
tieba_system/
├── tieba_system/          # 项目配置
│   ├── settings.py        # 项目设置
│   ├── urls.py            # 路由配置
│   └── wsgi.py           # WSGI配置
├── users/                 # 用户应用
│   ├── models.py         # 用户模型
│   ├── views.py          # 用户视图
│   ├── serializers.py    # 序列化器
│   └── admin.py          # 管理配置
├── forums/               # 贴吧应用
│   ├── models.py         # 贴吧模型
│   ├── views.py          # 贴吧视图
│   └── admin.py          # 管理配置
├── posts/                # 帖子应用
│   ├── models.py         # 帖子模型
│   ├── views.py          # 帖子视图
│   └── admin.py          # 管理配置
├── templates/            # 前端模板
├── static/               # 静态文件
├── media/                # 媒体文件
├── requirements.txt      # 依赖包
├── manage.py            # 管理脚本
└── .env.example         # 环境变量示例
```

## 快速开始

### 1. 环境准备

```bash
# 克隆项目
git clone <repository-url>
cd tieba-system

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置环境

```bash
# 复制环境变量文件
cp .env.example .env

# 编辑.env文件，配置数据库等信息
```

### 3. 数据库初始化

```bash
# 生成数据库迁移文件
python manage.py makemigrations

# 执行数据库迁移
python manage.py migrate

# 创建超级用户
python manage.py createsuperuser
```

### 4. 启动开发服务器

```bash
# 启动Django开发服务器
python manage.py runserver

# 访问应用
# 前端: http://localhost:8000
# 后台: http://localhost:8000/admin
```

## API接口

### 用户认证
- `POST /api/auth/login/` - 用户登录
- `POST /api/auth/logout/` - 用户登出
- `POST /api/auth/register/` - 用户注册
- `GET /api/auth/current/` - 获取当前用户信息

### 贴吧管理
- `GET /api/forums/` - 获取贴吧列表
- `POST /api/forums/` - 创建贴吧
- `GET /api/forums/{id}/` - 获取贴吧详情
- `PUT /api/forums/{id}/` - 更新贴吧信息

### 帖子管理
- `GET /api/posts/` - 获取帖子列表
- `POST /api/posts/` - 创建帖子
- `GET /api/posts/{id}/` - 获取帖子详情
- `PUT /api/posts/{id}/` - 更新帖子

## 部署说明

### 生产环境配置

1. 设置 `DEBUG=False`
2. 配置生产数据库（MySQL）
3. 配置Redis缓存
4. 配置静态文件和媒体文件存储
5. 使用Gunicorn + Nginx部署

### Docker部署

项目支持Docker容器化部署，具体配置参考 `docker-compose.yml` 文件。

## 开发指南

### 代码规范
- 遵循PEP 8编码规范
- 使用Black进行代码格式化
- 编写单元测试
- 添加适当的注释和文档

### 贡献指南
1. Fork项目
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建Pull Request

## 许可证

本项目采用MIT许可证。

## 联系方式

如有问题或建议，请联系项目维护者。