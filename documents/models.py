from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.shortcuts import reverse
# Create your models here.

def upload_to(instance, filename):
    return '%s/%s/%s' %('documents',instance.slug, filename)

class Document(models.Model):
    title = models.CharField(max_length=122)
    content = RichTextField(null=True, blank=True)
    slug = models.SlugField(max_length=122,default='',unique=True,null=False,blank=True,editable=False)
    file = models.FileField(upload_to=upload_to, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def get_slug(self):
        return self.slug

    @property
    def get_file_or_none(self):
        if self.file and hasattr(self.file,'url'):
            return self.file.url

    def unique_slug(self, new_slug, original_slug, index):
        if Document.objects.filter(slug=new_slug):
            new_slug = '%s-%s'%(original_slug,index)
            index += 1
            return self.unique_slug(new_slug=new_slug,original_slug=original_slug,index=index)
        return new_slug

    def save(self, *args, **kwargs):
        if self.slug == '':
            index = 1
            new_slug = slugify(self.title)
            self.slug = self.unique_slug(new_slug=new_slug,original_slug=new_slug,index=index)

        super(Document, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('documents:detail', kwargs={'slug': self.slug})

