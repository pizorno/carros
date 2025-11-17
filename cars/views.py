from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cars.models import Car
from cars.forms import CarModelForm


@login_required(login_url='login')
def cars_view(request):
    data = request.GET.get("search")
    if data:
        cars = Car.objects.filter(model__icontains=data).order_by("model")
    else:
        cars = Car.objects.all().order_by("-model")
    # cars = Car.objects.filter(brand__name='Chevrolet')
    return render(request, "cars.html", {"cars": cars})

@login_required(login_url='login')
def new_car_view(request):
    if request.method == "POST":
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect("cars_list")
    else:
        new_car_form = CarModelForm()
    return render(request, "new_car.html", {"form": new_car_form})