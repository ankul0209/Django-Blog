from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    content = models.TextField()
    timeStamp = models.DateField(blank=True)

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[0:15] + "..." + "by " + self.user.username
