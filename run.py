# coding:utf-8
import time
import os
from libs import search

os.system('python3 manage.py runserver 0.0.0.0:8000')

time.sleep(20)
search.init()
print('--swiper server ok---')