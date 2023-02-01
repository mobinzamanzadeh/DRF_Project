from datetime import timezone
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class Article(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    publish = models.DateTimeField(default=datetime.now(timezone.utc))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(False)

    def __str__(self):
        return self.title



