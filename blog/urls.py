from django.contrib import admin
from django.urls import path, include
from .views import ArticleList

urlpatterns = [
    path("", ArticleList.as_view(), name="list"),
    path("<int:pk>", ArticDetail.as_view(), name="detail"),
]
