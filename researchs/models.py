from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse

class CategoryResearch(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

    class Meta:
        ordering = ['category_name']

class ResearchManager(models.Manager):
    def get_three_items(self, *args, **kwargs):
        return super(ResearchManager, self).all()[:3]

class Research(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    content = RichTextField()
    category = models.ForeignKey(CategoryResearch, on_delete=models.SET_NULL, null=True, related_name='researchs')
    slug = models.SlugField(max_length=122,default='',unique=True,null=False,verbose_name='Slug Alanı',editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ResearchManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("research:show", kwargs={"slug": self.slug})
    

    def unique_slug(self,new_slug,orjinal_slug,index):
        if Research.objects.filter(slug=new_slug):
            new_slug = '%s-%s'%(orjinal_slug,index)
            index += 1
            return self.unique_slug(new_slug=new_slug,orjinal_slug=orjinal_slug,index=index)
        return new_slug

    def save(self, *args, **kwargs):

        if self.slug == '':
            index=1
            new_slug = slugify(self.title)
            self.slug=self.unique_slug(new_slug=new_slug,orjinal_slug=new_slug,index=index)
            

        super(Research, self).save(*args,**kwargs)


    class Meta:
        ordering = ['-created_at']

