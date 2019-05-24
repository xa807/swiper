from food import tasks
from common.http import render_json
from libs import cache


def qbuy(request):
    # 1. 验证用户是否已登录
    login_user = request.session.get('login_user', None)
    if login_user is None:
        return render_json(100, '当前用户未登录')

    # 2. 查询当前用户是否已抢
    if cache.is_qbuy(login_user.get('uid')):
        # 3. 调用异常任务，实现抢购
        food_id = request.GET.get('id')
        tasks.qbuy.delay(login_user.get('uid'), food_id)
        # 4. 给客户端返回接口数据
        return render_json(201, '正在抢购')

    return render_json(300, '抢购失败')


def query_qbuy_state(request):
    user_id = request.session['login_user'].get('uid')
    food_id = request.GET.get('id')
    # 从抢购结果中查询当前用户是否抢到
    # 1. 判断结果中是否存在当前用户的抢购记录
    # 2. 如果结果中已有当前用户，判断是否是一款商品
    # 限制当天用户只能抢一 次
    code, msg = cache.query_qbuy_state(user_id, food_id)

    return render_json(code, msg)
