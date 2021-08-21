from django.forms import ModelForm
from .models import Espresso, Coffee

class EspressoForm(ModelForm):
    
    class Meta:
        model = Espresso     
        fields = [
            "coffee_name", "water_temp", "water_tds", "batch_number", "dry_weight",
            "wet_weight", "extraction_time", "acidity_score", "acidity_quality", "aroma",
            "flavour_score", "flavour_quality", "texture", "texture_quality",
            "balance", "sweetness", "bitterness", "body",
            "finish", "notes",
        ]