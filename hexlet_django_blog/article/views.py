from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'app_name': 'Hexlet Django BLog',
        'page_title': 'Articles'
    }
    return render(request, 'article/index.html', context)