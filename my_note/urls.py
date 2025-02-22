from django.urls import path
from . import views

urlpatterns = [
    path('',views.my_semester,name="my_semester"), 
    path('semesters/<int:semester_id>/', views.semester_detail, name='semester_detail'),
    path('courses/<int:course_id>/', views.my_course_detail, name='my_course_detail'),
    path('create_document/<int:course_id>/', views.create_document, name='create_document'),
    path('upload_document_file/<int:document_id>', views.upload_document_file, name='upload_document_file'),
    path('add-course/<int:semester_id>/', views.add_course, name='add_course'), 

    path('courses/<int:id>',views.edit_document,name="edit_document"),
    # path('courses/<int:course_id>/',views.delete_document,name="delete_document"),
    path('courses/<int:course_id>/delete/<int:id>/', views.delete_document, name="delete_document"),
]