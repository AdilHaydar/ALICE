from django.db import models

# Create your models here.

def upload_to(instance,filename):
    return '%s/%s/%s' %('gallery',instance.gallery.name, filename)

class GalleryHeader(models.Model):
    name = models.CharField(verbose_name='Name', max_length=155)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    gallery = models.ForeignKey(to=GalleryHeader, on_delete=models.CASCADE, related_name='galleries')
    image = models.ImageField(upload_to=upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.gallery) + ' - ' + self.image.name

