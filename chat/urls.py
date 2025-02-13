from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', chat_view, name='home'),
    path('chat_view/', chat_view, name='chat_view'),
    path('loginPage/', loginPage, name="loginPage"),
    path('logoutPage/', logoutPage, name="logoutPage"),
    path('registerPage/', registerPage, name="registerPage"),
    path('historyPage/', historyPage, name="historyPage")

]
