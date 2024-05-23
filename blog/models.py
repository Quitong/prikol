from django.contrib.auth import get_user_model
from django.db import models

user = get_user_model()
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(user,models.CASCADE)

    def __str__(self):
        return 'Post'+self.title


class Comment(models.Model):
    text = models.TextField()
    to_post = models.ForeignKey(Post, models.CASCADE)

