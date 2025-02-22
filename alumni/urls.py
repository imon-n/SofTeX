from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.alumni_list, name='alumni_list1'),  # All alumni (default)
    path('alumni/session/<int:session_id>/', views.alumni_list, name='alumni_by_session'),  # Filter by session
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
