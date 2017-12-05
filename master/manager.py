#coding=utf-8

from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect

def m_login(request):
    return render(request, 'master/m_login.html')


#首页
def m_main(request):
    return render(request, 'master/m_main.html')

#车次管理
def m_checi(request):
    return render(request, 'master/m_checi.html')

#添加车次
def m_insert(request):
    return render(request, 'master/m_insert.html')

#路线管理
def m_route(request):
    return render(request, 'master/m_route.html')

#订单管理
def m_order(request):
    return render(request, 'master/m_order.html')

#车讯管理
def m_inform(request):
    return render(request, 'master/m_inform.html')

#公告管理
def m_announce(request):
    return render(request, 'master/m_announce.html')

#意见反馈
def m_suggest(request):
    return render(request, 'master/m_suggest.html')

