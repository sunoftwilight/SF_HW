from rest_framework import serializers
from .serializers import Article


class ArticleSerializer(__(b)__):

    class Meta:
        model = Article
        fields = '__all__'


# (b) : serializers.Modelserializer