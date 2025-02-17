from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.session_list, name='session_list'),
    # path('alumni/<int:session_id>/', views.alumni_list, name='alumni_list'),
    path('alumni/', views.alumni_list1, name='alumni_list1'),
    path('students/<int:session_id>/', views.current_students, name='student_list'),
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  