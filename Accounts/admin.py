from django.contrib import admin
from .models import *
from .forms import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,(
            'User role',
            {
                'fields':(
                    'is_user',
                    'is_doctor',
                    'is_driver',
                )
            }
        )
    )

admin.site.register(CustomUser,CustomUserAdmin)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user','phone','address','city','country','image_tag']
    list_filter = ['user']
    list_per_page = 10
    search_fields = ['user','phone','address']
    #inlines = [productImageInline]
    #prepopulated_fields = {'slug':('title',)}




admin.site.register(UserProfile,UserAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user','phone','address','city','country','image_tag']
    list_filter = ['user']
    list_per_page = 10
    search_fields = ['user','phone','address']
    #inlines = [productImageInline]
    #prepopulated_fields = {'slug':('title',)}




admin.site.register(DoctorProfile,DoctorAdmin)

class DriverAdmin(admin.ModelAdmin):
    list_display = ['user','phone','address','city','country','image_tag']
    list_filter = ['user']
    list_per_page = 10
    search_fields = ['user','phone','address']
    #inlines = [productImageInline]
    #prepopulated_fields = {'slug':('title',)}




admin.site.register(DriverProfile,DriverAdmin)
admin.site.register(HomeSlidding)