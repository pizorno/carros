from django.shortcuts import render
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
    new_car_form = CarForm()
    # if request.method == "POST":
    #     model = request.POST.get("model")
    #     brand = request.POST.get("brand")
    #     year = request.POST.get("year")
    #     image = request.FILES.get("image")

    #     Car.objects.create(model=model, brand_id=brand, year=year, image=image)

    return render(request, "new_car.html", {"form": new_car_form})