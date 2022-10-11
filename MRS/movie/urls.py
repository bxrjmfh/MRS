from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('recommendation/', views.get_user_movies, name='recommendation'),
    path('<slug:category_slug>/', views.movie_list, name='movie_list_by_category'),
    path('<int:id>/<slug:slug>/', views.movie_detail, name='movie_detail'),
]