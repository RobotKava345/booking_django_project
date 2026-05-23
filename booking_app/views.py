from django.shortcuts import render
from .models import Appartments, Booking

# Create your views here.
def home(request):
    appartments = Appartments.objects.all()
    return render(request, 'home.html', {'appartments': appartments})