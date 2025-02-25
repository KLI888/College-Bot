from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('chat_view/', chat_view, name='chat_view'),
    path('loginPage/', loginPage, name="loginPage"),
    path('logoutPage/', logoutPage, name="logoutPage"),
    path('registerPage/', registerPage, name="registerPage"),
    path('historyPage/', historyPage, name="historyPage"),
    path('feedbackPage/', FeedbackPageView.as_view(), name='feedback_page'),  # Make sure this name is 'feedback_page'
    path('feedback/success/', FeedbackSuccessView.as_view(), name='feedback_success'),

]
