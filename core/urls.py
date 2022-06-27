from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login',views.login, name = 'login'),
    path('<str:topic>/', views.topic, name='topic'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:topic>/', views.getMessages, name='getMessages'),
]