from datetime import datetime
from django.db import models


# Create your models here.
class User(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=256)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
