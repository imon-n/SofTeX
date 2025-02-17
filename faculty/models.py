from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200) 
    department = models.CharField(max_length=200) 
    email = models.EmailField()
    office_address = models.CharField(max_length=300)
    picture = models.ImageField(upload_to='faculty_pictures/', blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    academic_background = models.TextField() 
    area_of_interest = models.TextField(blank=True, null=True) 
    publications = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name



class AcademicBackground(models.Model):
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, related_name='academic_backgrounds')
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    passing_year = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"