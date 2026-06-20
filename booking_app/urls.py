from django.contrib import admin
from django.urls import path
from booking_app import views  
from django.conf import settings
from django.conf.urls.static import static


from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path(
        'appartment/<int:appartment_id>/',
        views.appartment_page,
        name='appartment_page'
    ),

    path(
        'booking/<int:appartment_id>/',
        views.booking_create,
        name='booking_create'
    ),

    path(
        'my_bookings/',
        views.my_bookings,
        name='my_bookings'
    ),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )