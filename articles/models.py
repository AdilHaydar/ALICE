from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.

class Article(models.Model):
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='Yazar')
    title = models.CharField(max_length=100, verbose_name='Title')
    content = RichTextField(verbose_name="Abstract")
    file = models.FileField(upload_to='articles', blank=True, null=True)
    slug = models.SlugField(max_length=122,default='',unique=True,null=False,blank=True,editable=False)
    view_count = models.IntegerField(default = 0, verbose_name = 'Görüntülenme Sayısı', editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

    @property
    def get_slug(self):
        return self.slug

    def unique_slug(self, new_slug, original_slug, index):
        if Article.objects.filter(slug=new_slug):
            new_slug = '%s-%s'%(original_slug,index)
            index += 1
            return self.unique_slug(new_slug=new_slug,original_slug=original_slug,index=index)
        return new_slug

    def save(self, *args, **kwargs):
        if self.slug == '':
            index = 1
            new_slug = slugify(self.title)
            self.slug = self.unique_slug(new_slug=new_slug,original_slug=new_slug,index=index)

        super(Article, self).save(*args, **kwargs)

    