from django.db import models

# Create your models here.

class MeetingReportCategory(models.Model):
    #meeting = models.ForeignKey(MeetingReport, on_delete=models.SET_NULL)
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.category_name}'

class MeetingReport(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name = 'metting_reports')
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='meeting_reports')
    category = models.ManyToManyField(MeetingReportCategory, related_name='categories', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField()

    class Meta:
        ordering= ['-date']

    def __str__(self):
        return self.title


class Meeting(models.Model):
    user = models.ForeignKey('auth.User', on_delete = models.CASCADE, related_name='meetings')
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to='meeting', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    
    def __str__(self):
        return self.title


