from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs ):
        return render(request, 'index.html')



def about(request):
    return render(request, "about.html")