from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.

def upload_to(instance, filename):
    return '%s/%s/%s'%('shifts',f'{instance.first_name}_{instance.last_name}',filename)



class AcademicTitle(MPTTModel):
    name = models.CharField(max_length=122, verbose_name='Title')
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    ordering = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by=['ordering']

class AuthorityTitle(models.Model):
    name = models.CharField(max_length=122)

    def __str__(self):
        return self.name


class ShiftManager(models.Manager):
    def get_shifts_without_authority(self, *args, **kwargs):
        return super(ShiftManager, self).filter(authority_title__isnull=True)
    
    def get_shifts_with_authority(self, *args, **kwargs):
        return super(ShiftManager, self).filter(authority_title__isnull=False)

class Shift(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=upload_to)
    academic_titles = models.ForeignKey(to=AcademicTitle, on_delete=models.SET_NULL, null=True, blank=True, related_name='shifts')
    authority_title = models.ForeignKey(to=AuthorityTitle, on_delete=models.SET_NULL, null=True, blank=True, related_name='shifts')
    objects = ShiftManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        ordering=['academic_titles']


class ShiftProfile(models.Model):
    shift = models.OneToOneField(Shift, on_delete=models.CASCADE)
    about = RichTextField(null=True, blank=True)
    slug = models.SlugField(max_length= 122, unique=True, null=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.shift)

    def unique_slug(self,new_slug,orjinal_slug,index):
        if ShiftProfile.objects.filter(slug=new_slug):
            new_slug = '%s-%s'%(orjinal_slug,index)
            index += 1
            return self.unique_slug(new_slug=new_slug,orjinal_slug=orjinal_slug,index=index)
        return new_slug

    def save(self, *args, **kwargs):

        if self.slug == '':
            index = 1
            new_slug = slugify(self.shift.first_name+'-'+self.shift.last_name)
            self.slug = self.unique_slug(new_slug=new_slug, orjinal_slug=new_slug,index=index)
        
        super(ShiftProfile, self).save(*args, **kwargs)

    @property
    def get_slug(self):
        return self.slug