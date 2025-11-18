from django.shortcuts import render, redirect
from django.views import View
from cars.models import Car
from cars.forms import CarModelForm
from django.views.generic import ListView

    
class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        qs = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            qs = qs.filter(model__icontains=search)
        return qs
    

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