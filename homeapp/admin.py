from django.contrib import admin
from homeapp.models import Contact, MeetRequest
# Register your models here.

admin.site.register(Contact)

@admin.register(MeetRequest)
class MeetRequestAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'rpr_name', 'rpr_post']