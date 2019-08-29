from django.shortcuts import render
from .models import Apartment, Room


def home(request):
	apartments = Apartment.objects.all()
	return render(request, 'core/home.html', {'apartments':apartments})


def apartments(request, pk):
	apartment_name = Apartment.objects.get(id=pk)
	rooms = apartment_name.rooms.all()
	args = {'apartment_name':apartment_name,
			'rooms':rooms}
	return render(request, 'core/apartments.html', args)
