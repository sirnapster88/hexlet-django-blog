from django.shortcuts import render, get_object_or_404
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages

from hexlet_django_blog.article.models import Article
from .forms import CommentArticleForm, ArticleForm



class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles,
            },
        )
    
class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(
            request,
            "articles/show.html",
            context={
                "article": article,
            },
        )
    

class CommentArticleView(View):
    # если метод POST, то мы обрабатываем данные
    def post(self, request, *args, **kwargs):
        form = CommentArticleForm(request.POST)  # Получаем данные формы из запроса
        if form.is_valid():  # Проверяем данные формы на корректность
            comment = ArticleComment(
                content=form.cleaned_data[
                    "content"
                ],  # Получаем очищенные данные из поля content
            )  #  и создаем новый комментарий
            comment.save()

    # если метод GET, то создаем пустую форму
    def get(self, request, *args, **kwargs):
        form = CommentArticleForm()  # Создаем экземпляр нашей формы
        return render(
            request, "comment.html", {"form": form}
        )  # Передаем нашу форму в контексте
    

class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, "articles/create.html", {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Статья успешно добавлена")
            return redirect('articles')
        messages.error(request, "Ошибка при добавлении статьи")
        return render(request, 'articles/create.html', {'form':form})
    

class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {'form':form, 'article_id':article_id})
    
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "Статья успешно отредактирована")
            return redirect('articles')
        messages.error(request,"Ошибка изменения статьи")
        return render(request, 'articles/update.html', {'form':form, 'article_id':article_id})
        
            
