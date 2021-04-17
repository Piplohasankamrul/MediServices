from django.contrib import admin
from .models import *
from mptt.admin import DraggableMPTTAdmin
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name','d_s_text','status','created_at','updated_at','image_tag']
    list_filter = ['name','created_at']
    list_per_page = 10
    search_fields = ['name','d_s_text','d_s_title']
    #inlines = [productImageInline]
    prepopulated_fields = {'slug':('d_s_text',)}
admin.site.register(Doctor,DoctorAdmin)
class DoctorCategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug':('title',)}
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = DoctorCategories.objects.add_related_count(
            qs,
            Doctor,
            'd_s_text',
            'products_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = DoctorCategories.objects.add_related_count(qs,
                                                Doctor,
                                                'd_s_text',
                                                'products_count',
                                                cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related doctors (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related doctors (in tree)'

admin.site.register(DoctorCategories,DoctorCategoryAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ['user','doctor_name','status','booking_date','booking_Time']
    list_filter = ['user','booking_date','booking_Time']
    list_per_page = 10
    search_fields = ['user','doctor_name','booking_date','booking_Time']

admin.site.register(Booking,BookingAdmin)