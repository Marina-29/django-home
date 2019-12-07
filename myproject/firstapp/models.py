from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=64, null=False)
    description = models.CharField(max_length=1024)

class Article(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    author = models.CharField(max_length=64, null=False)
    title = models.CharField(max_length=64, null=False)
    subtitle = models.CharField(max_length=256)
    text = models.CharField(max_length=64000, null=False)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField(max_length=64, null=False)
    text = models.CharField(max_length=1024, null=False)

# Create your models here.
