from blog.models import Article
from .serializers import ArticleSerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import ListCreateAPIView


# class ArticleList(ListAPIView):
# queryset = Article.objects.all()
# serializer_class = ArticleSerializer


class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
