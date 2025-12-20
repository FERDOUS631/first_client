from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.
admin.site.register(profile)
admin.site.register(about)
admin.site.register(Skill)
admin.site.register(logo)
admin.site.register(resume)
admin.site.register(contactMessage)
admin.site.register(HeroSection)


# class logoAdmin(admin.ModelAdmin):
#     list_display = ('write_logo', 'logo_image')
#     readonly_fields = ('logo_image_preview',)
#     fields = ('write_logo', 'logo_image', 'logo_image_preview')

#     def logo_image_preview(self, obj):
#         if obj.logo_image:
#             return format_html('<img src="{}" style="max-width: 200px; max-height: 200px;" />', obj.logo_image.url)
#         return "No image"

#     logo_image_preview.short_description = 'Logo Image Preview'
# admin.site.register(logo, logoAdmin)