#coding=utf8
"""Platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from front import views as user_views
from master import manager as manager_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #前台
    #前台注册
    url(r'^u_register', user_views.u_register,name='u_register'),
    #前台登录
    url(r'^u_login',user_views.u_login,name='u_login'),
    #忘记密码
    url(r'^u_forget',user_views.u_forget,name='u_forget'),
    #首页
    url(r'^u_main',user_views.u_main,name='u_main'),
    #在线订票
    url(r'^u_booking', user_views.u_booking,name='u_booking'),
    #购票
    url(r'^u_buy', user_views.u_buy,name='u_buy'),
    #帮助中心
    url(r'^u_help',user_views.u_help,name='u_help'),
    #个人中心
    url(r'^u_own',user_views.u_own,name='u_own'),
    url(r'^u_suggestion',user_views.u_suggestion,name='u_suggestion'),

    # # users:info
    # url(r'^user/', include('front.urls', namespace="users")),

    #后台
    #管理员登录
    url(r'^m_login', manager_view.m_login,name='m_login'),
    # #基础框架
    # url(r'^m_base', manager_view.m_base,name='m_base'),
    #首页
    url(r'^m_main', manager_view.m_main,name='m_main'),
    #车次管理
    url(r'^m_checi', manager_view.m_checi,name='m_checi'),
    #新增车次
    url(r'^m_insert', manager_view.m_insert,name='m_insert'),
    #路线管理
    url(r'^m_route', manager_view.m_route,name='m_route'),
    #订单管理
    url(r'^m_order', manager_view.m_order,name='m_order'),
    #车讯管理
    url(r'^m_inform', manager_view.m_inform,name='m_inform'),
    #帮助信息
    url(r'^m_help', manager_view.m_help,name='m_help'),
    #意见反馈
    url(r'^m_suggest', manager_view.m_suggest,name='m_suggest'),

]
