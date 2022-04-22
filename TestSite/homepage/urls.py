from django.urls import path
from .views import *

urlpatterns = [
    path('', MainHome.as_view(), name='home'),
    path('addpage/', AddTovar.as_view(), name="addpage"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),
    path('register/', RegisterUser.as_view(), name="register"),
    path('post-tovar/<slug:tovarslug>/', ShowTovar.as_view(), name='showtovar'),
    path('category/<slug:catslug>/', HomeCategory.as_view(), name='category'),
    path("password_reset", password_reset_request, name="password_reset"),
    path('validate_username', validate_username, name='validate_username')
]
