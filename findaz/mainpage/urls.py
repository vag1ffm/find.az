from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShopMainPage.as_view(), name='MainPage'),
]