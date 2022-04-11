from django.db import models
from django.urls import reverse
# Create your models here.
# 创建相关的电影类别：

class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    # 类别名称
    slug = models.SlugField(max_length=200,
                            unique=True)
    # 生成唯一的标识符

    class Meta:
        ordering = ('name',)
        app_label = 'movie'
        # 归属于movie 这一个 app
        verbose_name = 'category'
        # 定义可读名字
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    # 返回相应的url
    def get_absolute_url(self):
        return reverse('movie:movie_list_by_category',
                       args=[self.slug])
    # 在url中添加相应的标签。
    #     todo： 添加标签。path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),

class Director(models.Model):
    name = models.CharField(max_length=30)

class Actor(models.Model):
    name = models.CharField(max_length=30)

class Movie(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='movies',
                                 on_delete=models.CASCADE)
    # 外键为电影种类
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    # 电影的唯一标识
    image = models.ImageField(upload_to='movies/%Y/%m/%d',
                              blank=True)
    # 规定电影图片的上传路径，见文档 https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ImageField
    description = models.TextField(blank=True)
    # 可空的描述内容
    date = models.DateTimeField()
    # 电影的发布时间，可能有默认的属性可以设置
    directors = models.ManyToManyField(Director)
    actors = models.ManyToManyField(Actor)
    # 演员和导演

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    # 元数据，不知道怎么处理

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movie:product_detail',
                       args=[self.id, self.slug])

    def get_absolute_url(self):
        return reverse('movie:movie_detail',
                       args=[self.id, self.slug])

    #     todo： 添加标签。path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
