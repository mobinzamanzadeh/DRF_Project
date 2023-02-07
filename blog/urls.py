from django.contrib import admin
from django.urls import path, include
from .views import ArticleList, ArticleDetail

urlpatterns = [
    path("", ArticleList.as_view(), name="list"),
    path("<int:pk>", ArticleDetail.as_view(), name="detail"),
]
