from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path("tags/<str:tags>/<int:article_id>", views.IndexView.as_view(), name='articles'),
]