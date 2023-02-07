from rest_framework import serializers
from blog.models import Article
from django.contrib.auth.models import User


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "slug", "auther", "content", "publish", "status")

        # همه باشند به جز مواردی که می گویم:
        # exclude = ( "created", "updated")

        # همه باشند
        # fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

