from django.contrib import admin
from .models import Document, My_Document, DocumentFile

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'uploaded_at')
    search_fields = ('title', 'description')
    list_filter = ('course', 'uploaded_at')

admin.site.register(My_Document)
admin.site.register(DocumentFile)
