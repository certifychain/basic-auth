from django.urls import re_path
from . import views

urlpatterns = [
    re_path('login',views.login),
    re_path('signup',views.signup),
]
