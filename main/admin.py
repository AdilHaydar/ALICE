from django.contrib import admin
from .models import ContactInformation, Main, MainImage, Contact, Calendar
# Register your models here.


admin.site.register(Main)
admin.site.register(MainImage)
admin.site.register(ContactInformation)

class ContactAdmin(admin.ModelAdmin):
    list_filter = ('status',)

admin.site.register(Contact, ContactAdmin)
admin.site.register(Calendar)