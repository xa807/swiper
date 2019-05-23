from __future__ import absolute_import

from common.http import render_json
from libs import sms


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
    pass

