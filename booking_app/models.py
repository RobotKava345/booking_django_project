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

    title = models.CharField(max_length=100, verbose_name="Назва апартаментів")
    adress = models.CharField(max_length=200, verbose_name="Адреса")
    image = models.ImageField(upload_to='appartment_images/', blank=True, null=True, verbose_name="Зображення")
    description = models.TextField(null=True, blank=True, verbose_name="Опис")
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна за день")
    capasity = models.IntegerField(default=1, verbose_name="Місткість")
    type_room = models.CharField(max_length=50, choices=TYPE_ROOM_CHOICES, null=True, blank=True, verbose_name="Тип номеру" )

    def __str__(self):
        return f" Назва: {self.title} - Адреса: {self.adress} - Ціна: ₴{self.price_per_day} грн/день - Місткість номеру: {self.capasity} людини -  Тип номеру: {self.type_room}"

    class Meta:
        verbose_name = "Апартаменти"
        verbose_name_plural = "Апартаменти"
        ordering = ['title', 'price_per_day']


class Booking(models.Model):
    appartments = models.ForeignKey(Appartments, on_delete=models.CASCADE,verbose_name="Апартаменти")
    name = models.CharField(max_length=100, verbose_name="Ім'я")
    surname = models.CharField(max_length=100, verbose_name="Прізвище")
    email = models.EmailField(verbose_name="Електронна пошта")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефону")
    check_in_date = models.DateTimeField(verbose_name="Дата заселення")
    check_out_date = models.DateTimeField(verbose_name="Дата виселення")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Загальна ціна")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Користувач")

    def __str__(self):
        return f"Бронювання для {self.name} {self.surname} - {self.appartments.title} з {self.check_in_date} по {self.check_out_date}"
    
    class Meta:
        verbose_name = "Бронювання"
        verbose_name_plural = "Бронювання"
        ordering = ['-created_at']