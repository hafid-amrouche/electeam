from django.contrib import admin
from django.urls import path
from . import views 
from . import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home' ),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('login/', views.login, name='login'),
    path('admin-electeam/', views.admin, name='admin'),
    path('admin-electeam/profile/', views.profile, name='profile'),
    path('admin-electeam/services/', views.services, name='services'),
    path('admin-electeam/services/add/', views.add_service, name='add-service'),
    path('admin-electeam/delete-g-image/', views.delete_g_image, name='delete-g-image'),
    path('admin-electeam/delete-service/', views.delete_service, name='delete-service'),

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
