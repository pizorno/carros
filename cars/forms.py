from django import forms
from cars.models import Car

       
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
