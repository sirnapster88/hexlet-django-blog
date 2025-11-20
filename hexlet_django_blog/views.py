from django.shortcuts import render


def index(request):
    context={
            'who': 'World',
            'app_name': 'Hexlet Django Blog',
            'page_title': 'Main Page'
        }
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")