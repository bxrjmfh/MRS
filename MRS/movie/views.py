from django.shortcuts import render, get_object_or_404
from .models import Category, Movie,Director,Actor
# Create your views here.

def movie_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    # 返回全部类别，可以在后边的
    movies = Movie.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        movies = movies.filter(category=category)
    return render(request,
                  'movie/movie/list.html',
                  {'category': category,
                   'categories': categories,
                   'movies': movies})

def movie_detail(request,id,slug):
    movie = get_object_or_404(Movie,id=id,slug=slug)
    directors = movie.directors.all()
    return render(request,'movie/movie/detail.html',
                  {'movie':movie})

def get_user_movies(request):
    category = None
    categories = Category.objects.all()
    # 返回全部类别，可以在后边的
    movies = Movie.objects.all()
    # todo:添加筛选的逻辑
    return render(request,
           'movie/movie/userlist.html',
           {'category': category,
            'categories': categories,
            'movies': movies})
