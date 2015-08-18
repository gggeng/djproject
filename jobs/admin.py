from django.contrib import admin
from .models import Location
from .models import Job

# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    list_display = ("city", "state", "country")

class JobAdmin(admin.ModelAdmin):
	list_display = ("job_title", "corp_name", "location", "pub_date", "job_description")
	ordering = ["-pub_date"]
	search_fields = ("job_title", "job_description")
	list_filter = ("location",)

admin.site.register(Location,LocationAdmin)

admin.site.register(Job,JobAdmin)

