from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # comment_set = 


class Comment(models.Model):
    # id = 
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # post_id = 