from django.shortcuts import render, redirect
from django.views import View
from cars.models import Car
from cars.forms import CarModelForm


class CarView(View):
    def get(self, request):
        data = request.GET.get("search")
        if data:
            cars = Car.objects.filter(model__icontains=data).order_by("model")
        else:
            cars = Car.objects.all().order_by("-model")
        # cars = Car.objects.filter(brand__name='Chevrolet')
        return render(request, "cars.html", {"cars": cars})
    

class NewCarView(View):
    def get(self, request):
        form = CarModelForm()
        return render(request, "new_car.html", {"form": form})

    def post(self, request):
        form = CarModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("cars_list")
        return render(request, "new_car.html", {"form": form})