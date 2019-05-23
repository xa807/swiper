from django.urls import path

from user import views
from user.api import get_code

urlpatterns = [
    path('regist/', views.regist),
    path('code/', get_code),
    path('index/', views.to_index),
    path('login/',views.login),
    path('logout/',views.logout),

]
