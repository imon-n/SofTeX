from django.shortcuts import render
from .models import Session, Alumni

def alumni_list(request, session_id=None):
    sessions = Session.objects.all().order_by('-year')
    
    if session_id:
        selected_session = Session.objects.get(id=session_id)
        alumni = selected_session.alumni.all()
    else:
        selected_session = None
        alumni = Alumni.objects.all() 

    return render(request, 'alumni/alumni_list1.html', {
        'sessions': sessions, 
        'selected_session': selected_session,
        'alumni': alumni
    })

