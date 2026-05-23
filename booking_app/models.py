from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Appartments(models.Model):
    TYPE_ROOM_CHOICES = [
        ('single', 'Одиночний номер'),
        ('double', 'Двомісний номер'),  
        ('suite', 'Люкс'),
        ('family', 'Сімейний номер'),
        ('studio', 'Студія'),
        ('penthouse', 'Пентхаус'),        
    ]

    title = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    image = models.ImageField(upload_to='appartment_images/', blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    capasity = models.IntegerField(default=1)
    type_room = models.CharField(max_length=50, choices=TYPE_ROOM_CHOICES, null=True, blank=True)

    def __str__(self):
        return f" Назва: {self.title} - Адреса: {self.adress} - Ціна: ₴{self.price_per_day} грн/день - Місткість номеру: {self.capasity} людини -  Тип номеру: {self.type_room}"
    

class Booking(models.Model):
    appartments = models.ForeignKey(Appartments, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Бронювання для {self.name} {self.surname} - {self.appartments.title} з {self.check_in_date} по {self.check_out_date}"