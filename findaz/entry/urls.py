from django.urls import path
from . import views

urlpatterns = [
    path('', views.EntryPage.as_view(), name='EntryPage'),
]