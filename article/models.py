import uuid

from django.db import models


def generate_uuid_id():
    return uuid.uuid4().hex


# Create your models here.
class Article(models.Model):
    id = models.CharField(primary_key=True, max_length=64, default=generate_uuid_id, editable=False, verbose_name='id')
    title = models.CharField(max_length=64, verbose_name='标题')
    content = models.TextField(verbose_name='正文')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')


class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='标签')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    article = models.ManyToManyField(Article, related_name='tag')
