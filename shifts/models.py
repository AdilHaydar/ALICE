from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
# Create your models here.

def upload_to(instance, filename):
    return '%s/%s/%s'%('shifts',f'{instance.first_name}_{instance.last_name}',filename)

UNVAN_LISTESI = (
    ('0profdr','Prof. Dr.'),
    ('1docdr','Doç. Dr.'),
    ('2dr','Dr.'),
    ('3arastirmadr','Araştırma Görevlisi Dr.'),
    ('4arastirma','Araştırma Görevlisi'),
)

UST_UNVAN = (
    ('baskan','Grup Başkanı'),
    ('sorumlu','Fizik Sorumlusu'),
)
    

class Shift(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=upload_to)
    top_title = models.CharField(max_length=20,choices=UST_UNVAN, verbose_name='Görev', null=True, blank=True)
    academic_titles = models.CharField(max_length=20, choices=UNVAN_LISTESI, verbose_name='Ünvan', blank=True, null=True)

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