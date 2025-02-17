from django.db import models

class Semester(models.Model):
    name = models.CharField(max_length=100) 
    number = models.PositiveIntegerField() 
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200) 
    code = models.CharField(max_length=20) 
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='courses')
    def __str__(self):
        return self.name


class Routine(models.Model):
    semester = models.OneToOneField(Semester, on_delete=models.CASCADE, related_name='routine')
    title = models.CharField(max_length=200)
    files = models.FileField(upload_to='routines/')

    def __str__(self):
        return f"{self.semester.name} Routine"