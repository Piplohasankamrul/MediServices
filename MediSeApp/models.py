from django.db import models
from django.forms import ModelForm,TextInput,EmailInput

# Create your models here.
class Setting(models.Model):
    status = (
        ('True','True'),
        ('False','False'),
    )
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    fax = models.CharField(blank=True,max_length=50)
    email = models.EmailField(blank=True,null=True,max_length=50)
    smptserver = models.CharField(max_length=100)
    smtpemail = models.EmailField(blank=True,null=True,max_length=50)
    smptpassword = models.CharField(blank=True,max_length=50)
    smptport = models.CharField(blank=True,max_length=100)
    icon = models.ImageField(blank=True,null=True,upload_to='icon/')
    facebook = models.CharField(max_length=100,blank=True)
    instagram = models.CharField(max_length=100,blank=True)
    address = models.TextField()
    contact = models.TextField()
    reference = models.TextField()
    status = models.CharField(max_length=200,choices=status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    status = (
        ('New','New'),
        ('Read','Read'),
        ('Closed','Closed'),
    )
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True,null=True,max_length=40)
    subject = models.CharField(max_length=200,blank=True)
    message = models.TextField(max_length=1000,blank=True)
    status = models.CharField(max_length=200,choices=status,default='New')
    ip = models.CharField(max_length=100,blank=True)
    note = models.CharField(max_length=200,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta:
        model=ContactMessage
        fields=['name','email','subject','message']
        widgets={
            'name': TextInput(attrs={'class':'input','placeholder':'Name & Sure Name'}),
            'email': EmailInput(attrs={'class':'input','placeholder':'Write your Email'}),
            'subject': TextInput(attrs={'class':'input','placeholder':'Write your Subject'}),
            'message': TextInput(attrs={'class':'input','placeholder':'Write your message'}),
        }
