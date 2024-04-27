from os import name
from django.urls import path
from . import views

app_name="accounts"
urlpatterns = [
    # path('',views.accounts),
    path('signup',views.signup,name="signup"), # type: ignore
    path('login',views.login,name="login"), # type: ignore
    path('logout',views.logout,name="logout"), # type: ignore
]