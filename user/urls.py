from django.urls import path

from user import views
from user import api

urlpatterns = [
    path('regist/', views.regist),
    path('code/', api.get_code),
    path('upload_avatar/', api.upload_avatar),
    path('update_avatar/', api.update_avatar),
    path('index/', views.to_index),
    path('login/',views.login),
    path('logout/',views.logout),

]
