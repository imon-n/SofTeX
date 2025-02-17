from django.db import models
from courses.models import Course

class Document(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    files = models.FileField(upload_to='documents/', max_length=100, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='documents', default=1)
    def __str__(self):
        return self.title


class My_Document(models.Model):
    title = models.CharField(max_length=100) 
    already_studied = models.BooleanField(default=False) 
    date = models.DateField(auto_now=False, auto_now_add=False)
    about = models.TextField() 
    video = models.URLField(max_length=1000)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='my_documents')
    def __str__(self):
        return self.title

class DocumentFile(models.Model):
    document = models.ForeignKey(My_Document, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='documents/')  # PDF or image
    def __str__(self):
        return self.file.name
    