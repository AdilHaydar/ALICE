from django.db import models
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Main(models.Model):
    edited_user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    content = RichTextField()
    edited_at = models.DateTimeField(auto_now = True)


class MainImage(models.Model):
    main = models.ForeignKey(Main, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='Main_Images')
    added_at = models.DateTimeField(auto_now_add = True)

class Contact(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Full Name')
    email = models.EmailField()
    topic = models.CharField(max_length=100, verbose_name='Topic')
    message = models.TextField()
    status = models.BooleanField(default=False, verbose_name='Okundu')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic

class ContactInformation(models.Model):
    address = models.TextField()
    phone = PhoneNumberField()
    fax = models.CharField(max_length=50,null=True, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.address

class Calendar(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    #allDay = models.BooleanField(default=True)

    def __str__(self):
        return self.title