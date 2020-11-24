from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

admin.site.register(Flat)

#admin.site.register(Agent)
@admin.register(Agent)
class AgentAdmin(ImportExportActionModelAdmin):
    list_display = ("first_name", "last_name")
    list_filter =  ("first_name", "last_name")