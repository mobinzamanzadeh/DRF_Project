from blog.models import Article
from .serializers import ArticleSerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView


# class ArticleList(ListAPIView):
# queryset = Article.objects.all()
# serializer_class = ArticleSerializer


class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


# class ArticleDetail(RetrieveDestroyAPIView): # متد دیلیت و نمایش api ها وجود دارد و میتوان پاک کرد
    # queryset = Article.objects.all()
    # serializer_class = ArticleSerializer


# با تغییر متد های داخل کلاس میتوان قابلیت های کار با api مثل get, update رو اضافه کرد
