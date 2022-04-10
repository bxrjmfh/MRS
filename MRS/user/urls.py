from django.urls import path, include
from . import views

app_name = 'user'
urlpatterns = [
    # 用户界面
    path('', views.user_info, name='user_info'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
