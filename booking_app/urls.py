from django.contrib import admin
from django.urls import path
from booking_app import views  
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('appartment/<int:appartment_id>/', views.appartment_page, name='appartment_page'),
    
]

if settings.DEBUG:
    from django.conf import settings
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)