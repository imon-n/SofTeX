from django.shortcuts import render
from .models import NoticeModel

def notice(request):
    notices = NoticeModel.objects.all()
    return render(request, 'notices.html', {'notices': notices})
