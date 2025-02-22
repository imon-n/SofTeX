from django.shortcuts import render, redirect, get_object_or_404
from courses.models import Semester,Course
from courses.forms import CourseForm
from documents.models import My_Document
from documents.forms import My_DocumentForm,DocumentFileForm


def add_course(request, semester_id):
    semester = get_object_or_404(Semester, pk=semester_id)
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)  # Save and capture the course instance
            course.semester = semester  # Attach semester to the course
            course.save()
            return redirect('semester_detail', semester_id=semester_id)
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})


def upload_document_file(request, document_id):
    document = get_object_or_404(My_Document, pk=document_id)
    if request.method == 'POST':
        form = DocumentFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.document = document  # Link file to the document
            file.save()
            return redirect('my_course_detail', course_id=document.course.id)
    else:
        form = DocumentFileForm()
    return render(request, 'upload_document_file.html', {'form': form})


def my_semester(request):
    semesters = Semester.objects.all().order_by('number')
    return render(request, 'semester_list.html', {'semesters': semesters})

def semester_detail(request, semester_id):
    semester = get_object_or_404(Semester, pk = semester_id)
    courses = semester.courses.all() # Use related_name='courses' to get related courses
    return render(request, 'semester_detail.html', {'semester': semester, 'courses': courses})

def my_course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    documents = course.my_documents.all()
    if request.method == 'POST':
        # Check if the checkbox was clicked
        document_id = request.POST.get('document_id')
        already_studied = 'already_studied' in request.POST
        
        # Update the document's already_studied field
        if document_id:
            document = get_object_or_404(My_Document, pk=document_id)
            document.already_studied = already_studied
            document.save()
        # Redirect to avoid form resubmission
        return redirect('my_course_detail', course_id=course.id)
    return render(request, 'course_detail.html', {'course': course, 'documents': documents})


def create_document(request, course_id):
    course = get_object_or_404(Course,pk=course_id)
    if request.method == 'POST':
        form = My_DocumentForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)  # Save and capture the document instance
            document.course = course  # Attach course to the document
            document.save()
            return redirect('my_course_detail', course_id=course.id)
    else:
        form = My_DocumentForm()
    return render(request, 'create_document.html', {'form': form})


# def edit_document(request, id):
#     my_doc = My_Document.objects.get(pk=id)
#     my_doc_form = My_DocumentForm(instance=my_doc)

#     if request.method == 'POST':
#         my_doc_form = My_DocumentForm(request.POST, instance=my_doc)
#         if my_doc_form.is_valid():
#             my_doc_form.save()
#             return redirect('my_course_detail', course_id=my_doc.course.id)  # Pass course_id
#     return render(request, 'create_document.html', {'form': my_doc_form})


def edit_document(request, id):
    my_doc = get_object_or_404(My_Document, pk=id)  # Use get_object_or_404 for better error handling
    if request.method == 'POST':
        my_doc_form = My_DocumentForm(request.POST, instance=my_doc)
        if my_doc_form.is_valid():
            my_doc_form.save()
            return redirect('my_course_detail', course_id=my_doc.course.id)  # Pass course_id correctly
    else:
        my_doc_form = My_DocumentForm(instance=my_doc)

    return render(request, 'edit_document.html', {'form': my_doc_form})


def delete_document(request, course_id, id):
    my_doc = get_object_or_404(My_Document, pk=id)
    if request.method == "POST":
        my_doc.delete()
        return redirect('my_course_detail', course_id=course_id)  # Ensure correct redirection
    return render(request, 'confirm_delete.html', {'document': my_doc})

# def delete_document(request,id):
#     my_doc = My_Document.objects.get(pk=id)
#     my_doc.delete()
#     return redirect('my_course_detail')