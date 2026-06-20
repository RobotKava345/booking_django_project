import django
from django.shortcuts import render, get_object_or_404, redirect
from .models import Appartments, Booking
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):

    appartments = Appartments.objects.all()

    check_in = request.GET.get('check_in')
    check_out = request.GET.get('check_out')

    if check_in and check_out:

        booked_apartments = Booking.objects.filter(
            check_in_date__lt=check_out,
            check_out_date__gt=check_in
        ).values_list(
            'appartments_id',
            flat=True
        )

        appartments = appartments.exclude(
            id__in=booked_apartments
        )

    return render(
        request,
        'home.html',
        {
            'appartments': appartments
        }
    )



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

        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        check_in_date = request.POST.get('check_in_date')
        check_out_date = request.POST.get('check_out_date')

        existing_bookings = Booking.objects.filter(
            appartments=appartment,
            check_in_date__lt=check_out_date,
            check_out_date__gt=check_in_date
        
        )

           

        if existing_bookings.exists():
            messages.error(
                request,
                "Вибачте, ці апартаменти вже заброньовані на обрані дати. Будь ласка, оберіть інші дати."
            )
            return redirect('booking_create', appartment_id=appartment.id)
        else:
            booking = Booking.objects.create(
                appartments=appartment,
                name=name,
                surname=surname,
                email=email,
                phone_number=phone_number,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                total_price=appartment.price_per_day,
                user=request.user if request.user.is_authenticated else None
            )

            return render(
                request,
                'successful_booking.html',
                {
                    'appartment': appartment,
                    'booking': booking
                }
            )

    return render(
        request,
        'booking.html',
        {
            'appartment': appartment
        }
    )

@login_required
def my_bookings(request):
    return render(
        request,
        'my_bookings.html'
    )