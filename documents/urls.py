from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('<int:course_id>/', views.document_list, name='document_list'),
    path('<int:course_id>/upload/', views.upload_document, name='upload_document'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
