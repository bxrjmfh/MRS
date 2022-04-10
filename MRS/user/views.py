from django.shortcuts import render, redirect, HttpResponse

from .models import User
from .form import UserForm, RegisterForm
import hashlib


def hash_code(s, salt='mysite'):  # 加点“盐”
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


def index(request):
    return render(request, 'index.html')
# def index(request):
#     username = request.GET.get("username")
#     if username:
#         return render(request, "index.html")
#     else:
#         return redirect("/login/")


def user_info(request):
    return render(request, 'user/user_info.html')


def login(request):
    # 通过下面的if语句，我们不允许重复登录：
    # 默认返回的是False
    # if request.session.get('is_login', None):
    #     return redirect('user:user_info')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
                if user.password == hash_code(password):
                    # 通过下面的语句，我们往session字典内写入用户状态和数据：
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('user:user_info')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'user/login.html', locals())

    login_form = UserForm()
    return render(request, 'user/login.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect('index')
    request.session.flush()
    return redirect('index')


def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'user/register.html', locals())
            else:
                same_name_user = User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'user/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = User()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.sex = sex
                new_user.save()
                return redirect('user:login')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'user/register.html', locals())
