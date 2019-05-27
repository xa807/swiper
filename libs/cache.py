from redis import Redis

rd = Redis(host='redis', db=1)


def save_code(phone, code):
    rd.set(phone, code)
    rd.expire(phone, 120)  # 120秒存活期


def get_code(phone):
    if rd.exists(phone):
        return rd.get(phone)

    return None


def is_qbuy(uid):
    # 判断uid用户是否可以抢
    # 条件1： uid不存在， 条件2： 限量10份
    return not rd.hexists('swiper.food.qbuy', uid) or rd.hlen('swiper.food.qbuy') < 10


def add_qbuy(uid, food_id):
    is_existed = rd.exists('swiper.food.qbuy')

    # 存储抢购的结果
    rd.hset('swiper.food.qbuy', uid, food_id)

    # 如果是第一次使用swiper.food.qbuy对象，则设置它的有效时间
    if not is_existed:
        rd.expire('swiper.food.qbuy', 3600 * 24)


def query_qbuy_state(uid, food_id):
    if rd.hexists('swiper.food.qbuy', uid):
        qbuy_food_id = rd.hget('swiper.food.qbuy', uid).decode()  # 返回是 bytes
        if food_id == qbuy_food_id:
            return 200, '抢购成功'
        else:
            return 301, '一天只限一份'

    if rd.hlen('swiper.food.qbuy') >= 10:
        return 302, '已抢完'

    return 201, '抢购中'


def add_total_rank(food_id, amount=1):
    # 添加总排行
    rd.zincrby('swiper.total.rank',
               food_id,
               amount)


def get_total_rank(top_n=5):
    rank_list = rd.zrevrange('swiper.total.rank',
                             0, top_n-1, withscores=True)
    return [(id_.decode(), int(amount))
            for id_, amount in rank_list]
