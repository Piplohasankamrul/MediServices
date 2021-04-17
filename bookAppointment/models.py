from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.forms import ModelForm
from Accounts.models import CustomUser
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey
from multiselectfield import MultiSelectField
from django.forms import ModelMultipleChoiceField
# Create your models here.
class DoctorCategories(MPTTModel):
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

class Doctor(models.Model):
    Status = (('New','New'),
              ('Accepted','Accepted'),
              ('Rejected','Rejected'),)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    d_s_title = models.CharField(max_length=200,null=True)
    d_s_text = models.ForeignKey(DoctorCategories,on_delete=models.CASCADE)
    d1 = models.CharField(max_length=200,null=True)
    #phone = models.CharField(max_length=200,null=True)
    m_t = models.CharField(max_length=200,null=True)
    e_t = models.CharField(max_length=200,null=True)
    m_l = models.CharField(max_length=200,null=True)
    e_l = models.CharField(max_length=200,null=True)
    image = models.ImageField(null=True,blank=True,upload_to='doctor/')
    d2 = models.CharField(max_length=200,null=True)
    d3 = models.CharField(max_length=200,null=True)
    d4 = models.CharField(max_length=200,null=True)
    d5 = models.CharField(max_length=200,null=True)
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




class Booking(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Cancelled', 'Cancelled')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    doctor_name = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, blank=True)
    age = models.CharField(max_length=200, blank=True)
    booking_date=models.CharField(max_length=200)
    booking_Time=models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200, blank=True)
    status = models.CharField(choices=STATUS, max_length=20, default='New')
    ip = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name





