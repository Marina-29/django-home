from django.contrib import admin
from django.urls import path
from .views import articles_get, articles_post, articles_comment_post

urlpatterns = [
    path('articles/', articles_get),
    path('articles/create/', articles_post),
    path('articles/comment/', articles_comment_post),
]