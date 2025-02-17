from django.shortcuts import render, get_object_or_404
from .models import Faculty,AcademicBackground

def faculty_list(request):
    faculty_members = Faculty.objects.all()
    return render(request, 'faculty/faculty_list.html', {'faculty_members': faculty_members})

def faculty_list1(request):
    return render(request, 'faculty/faculty_list1.html')
    
def teacher_details(request, id):
    teacher = Faculty.objects.get(pk=id)
    academic_backgrounds = AcademicBackground.objects.all()
    return render(request, 'faculty/teacher_details.html', {'teacher': teacher, 
        'academic_backgrounds': academic_backgrounds
    })