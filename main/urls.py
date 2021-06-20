from django.urls import path
from . import views


urlpatterns = [
    path('add/',views.add,name='add'),
    path('get-main-data/',views.lazy_main,name='get-main-data'),
    path('get-announcement-data/',views.lazy_announcement,name='get-announcement-data'),
    path('contact/',views.contact,name='contact'),
    path('calendar/',views.calendar,name='calendar'),
    path('drag-event/',views.drag_event,name='drag-event'),
    path('add-new-event/',views.add_new_event,name='add-new-event'),
    path('update-event/',views.update_event, name='update-event'),
    path('delete-event/',views.delete_event,name='delete-event'),
]