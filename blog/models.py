
from django.contrib.auth import get_user_model
from django.db import models



User = get_user_model()
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User,models.CASCADE)

    def __str__(self):
        return 'Post'+self.title


class Comment(models.Model):
    text = models.TextField()
    to_post = models.ForeignKey(Post, models.CASCADE)
    author = models.ForeignKey(User, models.CASCADE)


class Quiz(models.Model):
    title = models.CharField(max_length=200)


class Question(models.Model):
    text = models.CharField(max_length=1000)
    to_quiz = models.ForeignKey(Quiz, models.CASCADE)


class Answer(models.Model):
    text = models.CharField(max_length=1000)
    to_question= models.ForeignKey(Question, models.CASCADE)

