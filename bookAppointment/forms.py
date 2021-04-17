from . import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from .models import *
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name','doctor_name',
                  'phone', 'address', 'city', 'country','booking_date','booking_Time','gender','age']


class DoctorRegister(ModelForm):
    class Meta:
        model=Doctor
        fields = ['name', 'd_s_title','d_s_text',
                  'd1', 'm_t', 'e_t', 'm_l','e_l','image','d2','d3','d4','d5']

        #def __init__(self, *args, **kwargs):
            #super(DoctorRegister, self).__init__(*args, **kwargs)
            #for field in self.fields:
                #self.fields[field].widget.attrs = {'class': 'form-control'}

class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
            'password': forms.PasswordInput()
        }