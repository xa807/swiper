from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from user.forms import UserForm
from user.models import User

from libs.cache import get_code
from libs.oss   import get_small_url

# Create your views here.
@csrf_exempt
def regist(request):
    if request.method == 'GET':
        return render(request, 'regist.html')

    # 处理post请求
    form = UserForm(request.POST)  # 将数据传入到Form类
    # 验证数据的完整性
    if form.is_valid():
        code = get_code(form.cleaned_data.get('phonenum'))
        if code.decode() == form.cleaned_data.get('code'):
            form.save()  # 无错时，则保存数据
            return redirect('/user/index/')
        else:
            return render(request, 'regist.html', {'errors': '<h4>验证码验证失败!</h4>'})

    errors = form.errors  # 默认情况是html的错误信息
    return render(request, 'regist.html', locals())

@csrf_exempt
def login(request):
    if request.method == 'POST':
        # 请求参数验证
        phonenum = request.POST.get('phonenum', None)
        code = request.POST.get('code', None)

        if phonenum is None or code is None:
            errors = '验证码或手机号不能为空'
        else:
            cache_code = get_code(phonenum).decode()
            if code == cache_code:
                # 验证成功，判断用户是否存在
                try:
                   login_user = User.objects.get(phonenum=phonenum)
                   avatar = login_user.avatar
                   request.session['login_user'] = {
                       'uid': login_user.id,
                       'nickname': login_user.nickname,
                       'avatar':  '/static/images/default.jpg' if avatar is None else get_small_url(avatar)
                   }

                   return redirect('/user/index/')

                except Exception as e:
                    errors = '%s 手机用户不存在，请先注册' % phonenum

    return render(request, 'login.html', locals())


def logout(request):
    request.session.pop('login_user')
    return redirect('/user/index/')


def to_index(request):
    return render(request, 'index.html')