from django.urls import reverse_lazy
from cars.models import Car
from cars.forms import CarModelForm
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin


class CarsListView(ListView):
    model = Car
    template_name = "cars.html"
    context_object_name = "cars"

    def get_queryset(self):
        qs = super().get_queryset().order_by("model")
        search = self.request.GET.get("search")
        if search:
            qs = qs.filter(model__icontains=search)
        return qs


class NewCarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CarModelForm
    template_name = "new_car.html"
    success_url = "/cars/"


class CarDetailView(DetailView):
    model = Car
    template_name = "car_detail.html"


class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = "car_update.html"

    def get_success_url(self):
        # return f'/car/{self.object.pk}/update/'
        return reverse_lazy("car_update", kwargs={"pk": self.object.pk})


class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = "car_delete.html"
    success_url = "/cars/"
