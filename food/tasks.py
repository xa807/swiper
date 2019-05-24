from swiper.celery import app
from libs import cache

@app.task
def qbuy(uid, food_id):
    # 查询用户是否可以抢购
    if cache.is_qbuy(uid):
        cache.add_qbuy(uid, food_id)

    return '%s 抢 %s 成功' % (uid, food_id)


