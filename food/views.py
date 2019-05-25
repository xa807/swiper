import random

import math
from django.shortcuts import render

from food.models import Food
from django.db import connection
# Create your views here.
from libs import cache


def all(request):
    # 分页算法
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('size', 20))

    total_pages = request.session.get('total_pages', None)
    if total_pages is None:
        c = connection.cursor()
        c.execute('select count(*) from t_food')
        total = c.fetchone()[0]
        total_pages = math.ceil(total/page_size)
        request.session['total_pages'] = total_pages
        print('totalpages: ', total_pages)

    # 页码范围
    page_range = range(page-2 if page-2 >= 1 else 1,
                       page+5 if page + 5 <= total_pages else total_pages)

    # 分页查询
    foods = Food.objects.raw('select * from t_food LIMIT %s, %s' %((page-1)*page_size, page_size))
    return render(request, 'food/list.html', locals())


def detail(request, id):
    # 点击排行-redis
    cache.add_total_rank(id)
    food = Food.objects.get(pk=id)

    # 查询前5的总排行
    rank_list = cache.get_total_rank()  # [('490', 1900)]
    rank_list = [(Food.objects.get(pk=id_), amount) for id_, amount in rank_list]

    return render(request, 'food/detail.html', locals())