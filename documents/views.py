from django.shortcuts import render, redirect, get_object_or_404
from .forms import DocumentForm
from courses.models import Course

# PersonalDocuments

def document_list(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    documents = course.documents.all()
    return render(request, 'documents/document_list.html', {'course': course, 'documents': documents})

def upload_document(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.course = course
            document.save()
            return redirect('document_list', course_id=course_id)
    else:
        form = DocumentForm()
    return render(request, 'documents/upload_document.html', {'form': form, 'course': course})

