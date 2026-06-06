from django.shortcuts import render, get_object_or_404
from .models import Appartments, Booking

# Create your views here.
def home(request):
    appartments = Appartments.objects.all()
    return render(request, 'home.html', {'appartments': appartments})

def appartment_page(request, appartment_id):
    appartment = get_object_or_404(
        Appartments,
        id=appartment_id
    )

    return render(
        request,
        'appartment_page.html',
        {'appartment': appartment}
    )


def booking_create(request, appartment_id):

    appartment = get_object_or_404(
        Appartments,
        id=appartment_id
    )

    if request.method == 'POST':

        Booking.objects.create(
            appartments=appartment,
            name=request.POST['name'],
            surname=request.POST['surname'],
            email=request.POST['email'],
            phone_number=request.POST['phone_number'],
            check_in_date=request.POST['check_in_date'],
            check_out_date=request.POST['check_out_date']
        )

        return redirect('home')

    return render(
        request,
        'booking.html',
        {'appartment': appartment}
    )