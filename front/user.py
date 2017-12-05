#coding=utf-8

from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect

from front.models import user

# Create your views here.

#注册
def u_register(request):
    if request.method == 'POST':
        phone = request.POST['rgphone']
        username = request.POST['rgname']
        pwd = request.POST['password']
        userphone = user.objects.filter(U_phone = phone)   #判断这个号码是否已经注册
        if not userphone:
            user.objects.create(U_phone = phone,U_pwd = pwd,U_name = username)
            return HttpResponseRedirect('/u_login/')
        else:
            return HttpResponseRedirect('/u_register/')
    return render(request, 'front/u_register.html')

#登录
def u_login(request):
    if request.method == 'POST':
        phone = request.POST['lgphone']
        pwd = request.POST['password']
        customer = user.objects.filter(U_phone = phone,U_pwd = pwd)
        if customer:
            response = HttpResponseRedirect('/first/')
            # 将username写入浏览器cookie，失效时间为3600
            # response.set_cookie('lgohone', phone,3600)
            return response
        else:
            #失败
            return HttpResponseRedirect( '/u_login/')
    return render(request, 'front/u_login.html')



#忘记密码
def u_forget(request):
    return render(request, 'front/u_forget.html')

#首页
def u_main(request):
    return render(request, 'front/u_main.html')

#在线订票
def u_booking(request):
    return render(request, 'front/u_booking.html')

#帮助信息
def u_help(request):
    return render(request, 'front/u_help.html')

#个人中心
def u_own(request):
    return render(request, 'front/u_own.html')

#投诉建议
def u_suggestion(request):
    return render(request, 'front/u_suggestion.html')

