from django import forms
from cars.models import Brand

class CarForm(forms.Form):
    model = forms.CharField(max_length=100, label="Modelo")
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), label="Marca")
    model_year = forms.IntegerField(label="Ano Modelo")
    factory_year = forms.IntegerField(label="Ano Fábricação")
    plate = forms.CharField(max_length=10, label="Placa", required=False)
    value = forms.FloatField(label="Valor", required=False)
    photo = forms.ImageField(label="Imagem", required=False)
