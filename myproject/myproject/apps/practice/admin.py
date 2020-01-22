from django.contrib import admin

from .models import Practice, Group, Student, Teacher, Enterprise

from import_export.admin import ImportExportModelAdmin

@admin.register(Practice, Group, Student, Teacher, Enterprise)
class ViewAdmin(ImportExportModelAdmin):
    pass
