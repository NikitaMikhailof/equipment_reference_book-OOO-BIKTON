from django.urls import path
from . import views 


app_name = "account"

urlpatterns = [
    path('login/', views.user_login, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
]