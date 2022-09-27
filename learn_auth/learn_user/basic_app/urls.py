from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('index', views.index, name='index'),
    path('registration', views.register, name='registration'),
    path('user_login', views.user_login, name='login'),
    path('user_logout', views.user_logout, name='logout'),
]