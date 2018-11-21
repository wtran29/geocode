from django.contrib import admin

# Register your models here.
from distance.status.forms import StatusForm
from distance.status.models import Status


class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', '__str__']
    form = StatusForm


admin.site.register(Status, StatusAdmin)
