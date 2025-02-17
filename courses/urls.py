from django.urls import path
from . import views

urlpatterns = [
    path('', views.semester_list, name='semester_list'),
    path('<int:semester_id>/', views.course_list, name='course_list'),
    path('<int:course_id>/detail/', views.course_detail, name='course_detail'),  # A view to show course details and options
]
