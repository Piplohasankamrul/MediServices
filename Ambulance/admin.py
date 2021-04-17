from django.contrib import admin
from .models import *
from mptt.admin import DraggableMPTTAdmin
# Register your models here.
class AmbulaceAdmin(admin.ModelAdmin):
    list_display = ['name','driver_name','location','phone','status','created_at','updated_at','image_tag']
    list_filter = ['name','created_at']
    list_per_page = 10
    search_fields = ['name','driver_name','Location ']
    #inlines = [productImageInline]
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Ambulace,AmbulaceAdmin)

class AmbulanceCategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug':('title',)}
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = AmbulanceCategory.objects.add_related_count(
            qs,
            Ambulace,
            'location',
            'products_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = AmbulanceCategory.objects.add_related_count(qs,
                                                        Ambulace,
                                                        'location',
                                                        'products_count',
                                                        cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related ambulances (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related ambulances (in tree)'

admin.site.register(AmbulanceCategory,AmbulanceCategoryAdmin)
admin.site.register(AmbulanceSlidding)