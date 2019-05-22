from django.urls import path

from user.views import regist, to_index
from user.api import get_code

urlpatterns = [
    path('regist/', regist),
    path('code/', get_code),
    path('index/', to_index)

]
