from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    image = models.ImageField(upload_to='posts')
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=5000)


    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'



class Comment(models.Model):
    auther = models.ForeignKey(to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=3000)



