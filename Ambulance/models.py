from django.db import models
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.conf import settings
from Accounts.models import CustomUser
from multiselectfield import MultiSelectField
from django.forms import ModelMultipleChoiceField
from Accounts.models import DriverProfile

# Create your models here.
class AmbulanceCategory(MPTTModel):
    status = (
        ('True','True'),
        ('False','False'),
    )
    parent = TreeForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='children')
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    image = models.ImageField(blank=True,upload_to='category/')
    status = models.CharField(max_length=200,choices=status)
    slug = models.SlugField(null=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title

class Ambulace(models.Model):
    Status = (('New','New'),
              ('Accepted','Accepted'),
              ('Rejected','Rejected'),)

    name = models.CharField(max_length=200,null=True)
    driver_name = models.CharField(max_length=200,null=True)
    location = models.ForeignKey(AmbulanceCategory,on_delete=models.CASCADE)
    #form_location=models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    image = models.ImageField(null=True,blank=True,upload_to='driver/')
    discription = models.CharField(max_length=200,null=True)
    status = models.CharField(max_length=200,choices=Status,default='New')
    slug = models.SlugField(null=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def get_name(self):
        return self.user.name


    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src = "{}" heights = "70" width = "60"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    def get_absolute_url(self,):
        return reverse('doctor_details',kwargs={'slug':self.slug})

class AmbulanceSlidding(models.Model):
    AmbulaceName = models.CharField(max_length=200)
    image = models.ImageField(blank=True,upload_to='slidder/')

    def __str__(self):
        return self.AmbulaceName

    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""
