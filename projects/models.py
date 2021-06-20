from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.shortcuts import reverse
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=122)
    content = RichTextField(null=True, blank=True)
    slug = models.SlugField(max_length=122,default='',unique=True,null=False,blank=True,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def get_slug(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"slug": self.slug})
    

    def unique_slug(self, new_slug, original_slug, index):
        if Project.objects.filter(slug=new_slug):
            new_slug = '%s-%s'%(original_slug,index)
            index += 1
            return self.unique_slug(new_slug=new_slug,original_slug=original_slug,index=index)
        return new_slug

    def save(self, *args, **kwargs):
        if self.slug == '':
            index = 1
            new_slug = slugify(self.title)
            self.slug = self.unique_slug(new_slug=new_slug,original_slug=new_slug,index=index)

        super(Project, self).save(*args, **kwargs)


    def __str__(self):
        return self.title