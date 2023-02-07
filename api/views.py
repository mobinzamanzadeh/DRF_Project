from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import *
from django.contrib.auth.models import User


# class ArticleList(ListAPIView):
# queryset = Article.objects.all()
# serializer_class = ArticleSerializer


class ArticleList(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # فیلدی که قرار است بر اساس اون انتخاب بشه و نمایش بدیم lookup_fields


# class ArticleDetail(RetrieveDestroyAPIView): # متد دیلیت و نمایش api ها وجود دارد و میتوان پاک کرد
# queryset = Article.objects.all()
# serializer_class = ArticleSerializer


# با تغییر متد های داخل کلاس میتوان قابلیت های کار با api مثل get, update رو اضافه کرد

class ArticleDelete(RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleUpdate(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleCreate(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
