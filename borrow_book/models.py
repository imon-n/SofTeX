from django.db import models

class Book_Model(models.Model):
  book_name = models.CharField(max_length=100)
  about = models.TextField(blank=True, null=True)
  image = models.ImageField(upload_to='book_images/')
  # phn = models.IntegerField(null=True, blank=True) 
  
  def __str__(self):
    return self.book_name 
