from django.shortcuts import render
from .forms import BookingForm # Make sure this import is correct
from .models import Booking
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'book.html', {'form': form, 'message': 'Booking successful!'})
        else:
            return render(request, 'book.html', {'form': form, 'error': 'Booking failed. Please check the form.'})
    return render(request, 'book.html', {'form': form})

@csrf_exempt
def bookings(request):
    if request.method == "POST":
        data = json.loads(request.body)
        exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(reservation_slot=data['reservation_slot']).exists()
        if not exist:
            booking = Booking(
                first_name=data['first_name'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
                name=data['name'],
                email=data['email'],
                phone=data['phone'],
                guests=data['guests'],
            )
            booking.save()
            return HttpResponse(content_type='application/json')
        else:
            return HttpResponse("{'error':1}", content_type='application/json')

    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)
    return HttpResponse(booking_json, content_type='application/json')