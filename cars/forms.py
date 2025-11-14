from django import forms
from cars.models import Brand, Car

class CarForm(forms.Form):
    model = forms.CharField(max_length=100, label="Modelo")
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), label="Marca")
    model_year = forms.IntegerField(label="Ano Modelo")
    factory_year = forms.IntegerField(label="Ano Fábricação")
    plate = forms.CharField(max_length=10, label="Placa", required=False)
    value = forms.FloatField(label="Valor", required=False)
    photo = forms.ImageField(label="Imagem", required=False)

    def save(self):
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        )
        car.save()
        return car
       
