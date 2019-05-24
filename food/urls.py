from django.urls import path

from food import views
from food import api

urlpatterns = [
    path('all/', views.all),
    path('qbuy/', api.qbuy),
    path('query_qbuy/', api.query_qbuy_state),
]
