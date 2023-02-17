from rest_framework import viewsets

from .permissions import IsSuperUser, IsStaffOrReadOnly, IsَAuthorOrReadOnly, IsَSuperuserOrStaffReadOnly
from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import *
from django.contrib.auth import get_user_model


# class ArticleList(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = IsStaffOrReadOnly


# class ArticleDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     # فیلدی که قرار است بر اساس اون انتخاب بشه و نمایش بدیم lookup_fields
#     permission_classes = IsStaffOrReadOnly, IsَAuthorOrReadOnly


# نوشتن view ها با view set
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.action in ['list', 'creat']:
            permission_classes = [
                IsStaffOrReadOnly,
            ]
        else:
            permission_classes = [IsStaffOrReadOnly, IsَAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


# با تغییر متد های داخل کلاس میتوان قابلیت های کار با api مثل get, update رو اضافه کرد

# class UserList(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSuperUser, IsَSuperuserOrStaffReadOnly)
#
#
# class UserDetail(RetrieveDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSuperUser, IsَSuperuserOrStaffReadOnly)

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        IsَSuperuserOrStaffReadOnly,
                          )
