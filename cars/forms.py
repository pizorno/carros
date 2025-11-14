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
       
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        #fields = ['model', 'brand', 'factory_year', 'model_year', 'plate', 'value', 'photo']
        labels = {
            'model': 'Modelo',
            'brand': 'Marca',
            'factory_year': 'Ano Fábricação',
            'model_year': 'Ano Modelo',
            'plate': 'Placa',
            'value': 'Valor',
            'photo': 'Imagem',
        }

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value is not None and value <= 0:
            self.add_error('value', 'O valor deve ser maior que zero.')
        return value
    
    def clean_factory_year(self):   
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year <= 1974:
            self.add_error('factory_year', 'O ano de fabricação não pode ser menor que 1974.')
        return factory_year
