from django.shortcuts import render, get_object_or_404
from .models import Alumni, Session, Current_Student

def session_list(request):
    alumni_sessions = Session.objects.filter(alumni__isnull=False).distinct().order_by('year')
    student_sessions = Session.objects.filter(current_student__isnull=False).distinct().order_by('year')
    return render(request, 'alumni/session_list.html', {'alumni_sessions': alumni_sessions, 'student_sessions': student_sessions})

def alumni_list(request, session_id):
    try:
        session = Session.objects.get(id=session_id)
        alumni = session.alumni.all()
        return render(request, 'alumni/alumni_list.html', {'session': session, 'alumni': alumni})
    except Session.DoesNotExist:
        return render(request, 'alumni/session_not_found.html', status=404)
    
def alumni_list1(request):
    return render(request, 'alumni/alumni_list1.html')


def current_students(request, session_id):
    try:
        session = Session.objects.get(id=session_id)
        students = session.current_student.all().order_by('student_id')
        return render(request, 'alumni/current_students.html', {'session': session, 'students': students})
    except Session.DoesNotExist:
        return render(request, 'alumni/session_not_found.html', status=404)
