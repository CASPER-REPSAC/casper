from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey('accounts.User', related_name='posts', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    viewer_num = models.IntegerField(default=0)
    category = models.ForeignKey('board.Category', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        ordering = ['created_date']
