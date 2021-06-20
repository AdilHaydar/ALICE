from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class SSS(models.Model):
    title= models.CharField(max_length=255)
    question=RichTextField()
    
    
