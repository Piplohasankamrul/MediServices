from . import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class AmbulanceRegister(ModelForm):
    class Meta:
        model=Ambulace
        fields = ['name', 'driver_name','location',
                  'phone','image','discription']

