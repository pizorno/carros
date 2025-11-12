from django.shortcuts import render
from cars.models import Car


def cars_view(request):
    # cars = Car.objects.all()
    cars = Car.objects.filter(brand__name='Chevrolet')
    return render(request, "cars.html", {"cars": cars})

