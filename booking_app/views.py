from django.shortcuts import render
from .models import Appartments, Booking

# Create your views here.
def home(request):
    appartments = Appartments.objects.all()
    return render(request, 'home.html', {'appartments': appartments})

def appartment_page(request, appartment_id):
    appartment = Appartments.objects.get(id=appartment_id)
    return render(request, 'appartment_page.html', {'appartment': appartment})