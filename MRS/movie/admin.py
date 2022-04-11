from django.contrib import admin
from .models import Movie,Actor,Category,Director
# Register your models here.

admin.site.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}