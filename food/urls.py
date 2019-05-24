from django.urls import path

from food import views
from food import api

urlpatterns = [
    path('all/', views.all),


]
