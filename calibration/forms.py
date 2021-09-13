from django.forms import ModelForm
from .models import Espresso, Coffee, Filter

class EspressoForm(ModelForm):
    
    class Meta:
        model = Espresso     
        exclude = ["user"]

class FilterForm(ModelForm):
    class Meta: 
        model = Filter
        exclude = ["user"]