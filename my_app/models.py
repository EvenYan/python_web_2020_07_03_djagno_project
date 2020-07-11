from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()

    def __str__(self):
        return self.title


class Score(models.Model):
    name = models.CharField(max_length=10)
    math = models.PositiveIntegerField()
    chinese = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    passwd = models.CharField(max_length=400)

    def __str__(self):
        return self.username