from articles.models import upload_to
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

def upload_to(instance, filename):
    return '%s/%s/%s' %('News',instance.slug,filename)

class News(models.Model):
    title = models.CharField(max_length=155, verbose_name='Title')
    content = RichTextField(verbose_name='News')
    slug = models.SlugField(max_length=155,default='',unique=True, null=False, blank=False, editable=False)
    image = models.ImageField(upload_to=upload_to, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def get_image(self):
        if self.image and hasattr(self.image,'url'):
            return self.image.url
        return '/static/images/newspaper.jpg'

    def __str__(self):
        return self.title

    def unique_slug(self,new_slug,orjinal_slug,index):
        if News.objects.filter(slug=new_slug):
            new_slug = '%s-%s'%(orjinal_slug,index)
            index += 1
            return self.unique_slug(new_slug=new_slug,orjinal_slug=orjinal_slug,index=index)
        return new_slug

    def save(self, *args, **kwargs):

        if self.slug == '':
            index=1
            new_slug = slugify(self.title)
            self.slug=self.unique_slug(new_slug=new_slug,orjinal_slug=new_slug,index=index)

        super(News, self).save(*args,**kwargs)


    
