from django.contrib import admin
from .models import MeetingReport, MeetingReportCategory, Meeting
# Register your models here.
admin.site.register(Meeting)

admin.site.register(MeetingReport)
admin.site.register(MeetingReportCategory)
