from django.shortcuts import render
from django.views.generic import ListView
from .models import Article


class ArticleList(ListView):
    def get_queryset(self):
        return Article.objects.filter(status=True)
    
    

class ArticDetail(DetailView):
    def get_object(self):
        return get_object_or_404(
            Article,
            pk=self.kwargs.get("pk"),
        )
