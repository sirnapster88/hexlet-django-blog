from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs ):
        reveresed_article = reverse('articles', kwargs={'tags': 'python', 'article_id': 42})
        return redirect(reveresed_article)



def about(request):
    return render(request, "about.html")