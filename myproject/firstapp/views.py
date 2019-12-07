from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def articles_get(request):
    return HttpResponse('get articles')

def articles_post(request):
    return HttpResponse('create an article')

def articles_comment_post(request):
    return HttpResponse('create comment to the article')