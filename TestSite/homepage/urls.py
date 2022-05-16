from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', MainHome.as_view(), name='home'),
    # path('addtovar/', login_required(AddTovar.as_view()), name="addtovar"),
    path('addtovar/', addtovar, name="addtovar"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),
    path('register/', RegisterUser.as_view(), name="register"),
    path('seller_register/', RegisterSeller.as_view(), name="register_seller"),
    # path('post-tovar/<slug:tovarslug>/', ShowTovar.as_view(), name='showtovar'),
    path('post-tovar/<slug:tovarslug>/', show_tovar, name='showtovar'),
    path('category/<slug:catslug>/', HomeCategory.as_view(), name='category'),
    path('category/<slug:catslug>/<slug:podcatslug>/', HomeCategory.as_view(), name='podcategory'),
    path('category/<slug:catslug>/<slug:podcatslug>/<slug:podpodcatslug>/', HomeCategory.as_view(), name='podpodcategory'),
    path("password_reset/", password_reset_request, name="password_reset"),
    path('validate_username/', validate_username, name='validate_username'),
    path('crud_favorites/', crud_favorites, name='crud_favorites'),
    path('confirm_email/', TemplateView.as_view(template_name='homepage/confirm_email.html'), name='confirm_email'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
    path('invalid_verify/', TemplateView.as_view(template_name='homepage/invalid_verify.html'), name='invalid_verify'),
]
