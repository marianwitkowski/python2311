from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "imdb")
    list_filter = ("year", )
    search_fields = ("title", "description")
    
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()
        #super(MovieAdmin, self).save_model(request, obj, form, change)

#admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor)
admin.site.register(Comment)

#####################################
admin.site.site_header = "Filmoteka"
admin.site.site_title = "Filmoteka Admin Panel"
admin.site.index_title = "Witamy w Filmotece"