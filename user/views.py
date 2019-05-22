from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from user.forms import UserForm
from libs.cache import get_code

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


def to_index(request):
    return render(request, 'index.html')