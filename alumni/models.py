from django.db import models

class Session(models.Model):
    year = models.CharField(max_length=10)
    def __str__(self):
        return self.year

class Alumni(models.Model):
    name = models.CharField(max_length=200)
    current_position = models.CharField(max_length=200,blank=True, null=True) 
    picture = models.ImageField(upload_to='faculty_pictures/', blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    email = models.EmailField(blank = True, null=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='alumni')

    def __str__(self):
        return self.name


class Current_Student(models.Model):
    name = models.CharField(max_length=200)
    student_id = models.IntegerField()
    picture = models.ImageField(upload_to='faculty_pictures/', blank=True, null=True)
    # linkedin = models.URLField(blank=True, null=True)
    email = models.EmailField(blank = True, null=True)
    interested_fields = models.TextField()
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='current_student')

    def __str__(self):
        return self.name