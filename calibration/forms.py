from django.forms import ModelForm
from .models import Espresso, Coffee, Filter

class EspressoForm(ModelForm):
    
    class Meta:
        model = Espresso     
        fields = "__all__"

class FilterForm(ModelForm):
    class Meta: 
        model = Filter
        fields = "__all__"