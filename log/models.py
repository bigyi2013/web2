from django.db import models
class log(models.Model):
    name=models.CharField(max_length=20)
    body=models.TextField(max_length=200)
    created_time = models.DateTimeField()
    def __str__(self):
        return self.name
class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey('blog.article',on_delete=models.CASCADE)
    def __str__(self):
        return self.text[:20]
# Create your models here.
