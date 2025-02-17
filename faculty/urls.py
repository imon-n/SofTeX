from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.faculty_list, name='faculty_list'),
    path('', views.faculty_list1, name='faculty_list1'),
    path('details/<int:id>', views.teacher_details, name='teacher_details'),
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  