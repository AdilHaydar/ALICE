from django.db import models

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
    academic_titles = models.CharField(max_length=20, choices=UNVAN_LISTESI, verbose_name='Ünvan')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        ordering=['academic_titles']