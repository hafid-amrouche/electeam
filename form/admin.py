from django.contrib import admin
from .models import ContactUs, Service, ServiceImage, INFO, GalleryImage
# Register your models here.

admin.site.register(ContactUs)
admin.site.register(ServiceImage)
admin.site.register(GalleryImage)
admin.site.register(Service)
admin.site.register(INFO)
