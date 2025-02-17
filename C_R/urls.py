from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="indexpage"),
    path('home/',views.home,name="homepage"),
    path('courses/', include('courses.urls')),  # Include the courses app URLs
    path('documents/', include('documents.urls')),  # Include the documents app URLs
    path('users/', include('users.urls')),  # Include the users app URLs
    path('alumni/', include('alumni.urls')),  # Include the alumni app URLs
    path('faculty/', include('faculty.urls')),  # Include the faculty app URLs
    path('my_note/', include('my_note.urls')),  # Include the my_note app URLs
    path('borrow_book/', include('borrow_book.urls')),  # Include the borrow_book app URLs
    path('notice/', include('notice.urls')),  # Include the notice app URLs
]


if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  