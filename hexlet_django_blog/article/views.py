from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class IndexView(View):
    template_name = 'article/index.html'

    def get(self, request, *args, **kwargs):
        context = {
        'app_name': 'Hexlet Django BLog',
        'page_title': 'Articles',
        'articles': []
    }
        return render(request, self.template_name, context)