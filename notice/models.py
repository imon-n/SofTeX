from django.db import models

class NoticeModel(models.Model):
    title = models.CharField(max_length=100)
    about = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title