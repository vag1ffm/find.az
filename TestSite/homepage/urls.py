from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    # path('', MainHome.as_view(), name='home'),
    path('', mainhome, name='home'),
    path('addtovar/', addtovar, name="addtovar"),
    path('accounts/login/', LoginUser.as_view(), name="login"),
    path('accounts/logout/', logout_user, name="logout"),
    path('accounts/register/', RegisterUser.as_view(), name="register"),
    path('accounts/seller_register/', RegisterSeller.as_view(), name="register_seller"),
    path('accounts/profile/<slug:place_slug>', show_profile, name="profile"),
    path('post-tovar/<slug:tovarslug>/', show_tovar, name='showtovar'),
    path('podpodcategory/<slug:podpodcatslug>/', HomeCategory.as_view(), name='podpodcategory'),
    path('podcategory/<slug:podcatslug>/', p_in_between, name='podcategory'),
    path('category/<slug:catslug>/', in_between, name='category'),
    path('filter_of_tovar', filter_of_tovar, name="filter_of_tovar"),
    path("password_reset/", password_reset_request, name="password_reset"),
    path('validate_username/', validate_username, name='validate_username'),
    path('crud_favorites/', crud_favorites, name='crud_favorites'),
    path('favorites/', show_favorites, name='show_favorites'),
    path('confirm_email/', TemplateView.as_view(template_name='homepage/confirm_email.html'), name='confirm_email'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
    path('invalid_verify/', TemplateView.as_view(template_name='homepage/invalid_verify.html'), name='invalid_verify'),
    path('find/', find, name="find")
]
