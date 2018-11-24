from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

from . import models


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.Article
