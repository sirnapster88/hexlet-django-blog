from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class IndexView(View):
    template_name = 'article/index.html'

    def get(self, request, tags, article_id, *args, **kwargs):
        text = f"Статья номер {article_id}. Тег {tags}"
        context = {
            'text': text,    
            'tags': tags,
            'article_id': article_id
    }
        #return HttpResponse(text)
        return render(request, self.template_name, context)