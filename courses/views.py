from django.shortcuts import render, get_object_or_404
from .models import Semester, Course

def semester_list(request):
    semesters = Semester.objects.all().order_by('number')
    return render(request, 'courses/semester_list.html', {'semesters': semesters})


def course_list(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)
    courses = semester.courses.all()
    routine = semester.routine if hasattr(semester, 'routine') else None
    return render(request, 'courses/course_list.html', {'semester': semester, 'courses': courses, 'routine': routine})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})