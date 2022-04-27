from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', MainHome.as_view(), name='home'),
    path('addpage/', AddTovar.as_view(), name="addpage"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),
    path('register/', RegisterUser.as_view(), name="register"),
    path('seller_register/', RegisterSeller.as_view(), name="register_seller"),
    path('post-tovar/<slug:tovarslug>/', ShowTovar.as_view(), name='showtovar'),
    path('category/<slug:catslug>/', HomeCategory.as_view(), name='category'),
    path("password_reset/", password_reset_request, name="password_reset"),
    path('validate_username/', validate_username, name='validate_username'),
    path('confirm_email/', TemplateView.as_view(template_name='homepage/confirm_email.html'), name='confirm_email'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
    path('invalid_verify/', TemplateView.as_view(template_name='homepage/invalid_verify.html'), name='invalid_verify'),
]
