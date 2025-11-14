from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm


def cars_view(request):
    data = request.GET.get("search")
    if data:
        cars = Car.objects.filter(model__icontains=data).order_by("model")
    else:
        cars = Car.objects.all().order_by("-model")
    # cars = Car.objects.filter(brand__name='Chevrolet')
    return render(request, "cars.html", {"cars": cars})

def new_car_view(request):
    if request.method == "POST":
        new_car_form = CarForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect("cars_list")
    else:
        new_car_form = CarForm()
    return render(request, "new_car.html", {"form": new_car_form})