from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

from . import models


class ArticleTagSerializer(serializers.ModelSerializer):
    article = serializers.CharField()
    tag = serializers.CharField()

    class Meta:
        fields = ('article', 'tag', 'create_time')
        model = models.ArticleTag


class TagSerializer(serializers.ModelSerializer):
    article = ArticleTagSerializer(many=True)

    class Meta:
        fields = '__all__'
        model = models.Tag


class ArticleSerializer(serializers.ModelSerializer):
    tag = ArticleTagSerializer(many=True)

    class Meta:
        fields = '__all__'
        model = models.Article
