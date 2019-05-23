from __future__ import absolute_import

import os
import uuid

from django.core.files.uploadedfile import InMemoryUploadedFile

from common.http import render_json
from libs import sms
from libs import oss
from swiper import settings
from user.models import User

def get_code(request):
    if request.method == 'GET':
        # 获取查询参数 phonenum
        print(request.GET)
        phonenum = request.GET.get('phonenum', None)

        if phonenum is None:
            return render_json(201, '请求参数phonenum是必填项')

        sms.new_code(phonenum)
        return render_json(200, '获取验证码成功!')

    return render_json(100,  '只允许GET请求')


def upload_avatar(request):
    # 上传用户头像
    if request.method == 'POST':
        avatar_file: InMemoryUploadedFile = request.FILES.get('avatar')  # 要求：前端上传头像的字段为avatar

        # 将上传的图片文件写入到临时文件中
        filedir = os.path.join(settings.BASE_DIR, 'static/images')
        filename = uuid.uuid4().hex + os.path.splitext(avatar_file.name)[-1]
        with open(os.path.join(filedir,filename), 'wb') as f:
            for chunk in avatar_file.chunks():
                f.write(chunk)
        return render_json(200,  {'path': '/static/images/%s' % filename})

    return render_json(300,  '只允许POST请求')


def update_avatar(request):
    if request.method == 'GET':
        filename = request.GET.get('filename')
        key = oss.upload_file(settings.BASE_DIR+filename)

        login_user = request.session['login_user']
        login_user['avatar'] = oss.get_small_url(key)

        user = User.objects.get(pk=login_user.get('uid'))
        user.avatar = key
        user.save()  # 更新头像的oss的key

        # 删除临时文件
        os.remove(settings.BASE_DIR+filename)

        return render_json(200, {'url': login_user['avatar'],
                                 'msg': '更新头像成功'})

    return render_json(100,  '只允许GET请求')