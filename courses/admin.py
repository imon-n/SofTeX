from django.contrib import admin
from .models import Semester, Course, Routine

admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(Routine)



# from django.contrib import admin
# from .models import Semester, Course

# @admin.register(Semester)
# class SemesterAdmin(admin.ModelAdmin):
#     list_display = ('name', 'number')
#     search_fields = ('name',)
#     ordering = ('number',)

# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('name', 'code', 'semester')
#     search_fields = ('name', 'code')
#     list_filter = ('semester',)

# @admin.register(Routine)
# class RoutineAdmin(admin.ModelAdmin):
#     list_display = ('title', 'semester', 'file_link')
#     search_fields = ('title', 'semester__name')
#     list_filter = ('semester',)
#     ordering = ('semester__number',)

#     def file_link(self, obj):
#         if obj.file:
#             return format_html('<a href="{}" target="_blank">Download</a>', obj.file.url)
#         return "No file available"
#     file_link.short_description = 'Routine File'





# courses/admin.py


