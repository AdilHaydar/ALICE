from django.contrib import admin
from .models import Shift, ShiftProfile, AcademicTitle, AuthorityTitle
from mptt.admin import DraggableMPTTAdmin
# Register your models here.

admin.site.register(Shift)
admin.site.register(ShiftProfile)
admin.site.register(
    AcademicTitle,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)
admin.site.register(AuthorityTitle)