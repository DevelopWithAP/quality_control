from django.forms import ModelForm
from .models import Espresso, Coffee

class EspressoForm(ModelForm):
    
    class Meta:
        model = Espresso     
        fields = "__all__"