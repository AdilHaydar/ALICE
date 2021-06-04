from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.

class AnnouncementManager(models.Manager):
    def get_publish_announcement(self, *args, **kwargs):
        return super(AnnouncementManager, self).filter(deadline_at__gt = timezone.now())

class Announcement(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=122, null=False, blank=False)
    announcement = RichTextField()
    created_at = models.DateTimeField(auto_now_add = True)
    deadline_at = models.DateTimeField()
    objects = AnnouncementManager()
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title