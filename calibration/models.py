from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

ACIDITY = (
    ("Delicate","Delicate"),
    ("Mild","Mild"),
    ("Nippy","Nippy"),
    ("Piquant","Piquant"),
    ("Sweet","Sweet"),
    ('Tangy', 'Tangy'),
    ('Tart', 'Tart'),
    ('Lemon','Lemon'),
    ('Vibrant', 'Vibrant'),
    ('Grassy', 'Grassy'),
    ('Hard', 'Hard'),
    ('Soft', 'Soft'),
    ('Sour', 'Sour'),
    ('Winey', 'Winey'),
    ('Grapefruit', 'Grapefruit'), 
)

AROMAS = (
    ('Berry', 'Berry'),
    ('Floral', 'Floral'),
    ('Fruity', 'Fruity'),
    ('Caramel', 'Caramel'),
    ('Resinous', 'Resinous'),
    ('Lemon', 'Lemon'),
    ('Grapefruit', 'Grapefruit'),
    ('Chocolate', 'Chocolate'),
    ('Spicy', 'Spicy'),
    ('Earthy', 'Earthy'),
    ('Nutty', 'Nutty'),
    ('Malty', 'Malty'),
    ('Carbonic', 'Carbonic'),
    ('Pepper', 'Pepper'),
    ('Vanilla', 'Vanilla'),
    ('Hidy', 'Hidy'),
    ('Musty', 'Musty'),
    ('Leather', 'Leather'),
    ('Butter', 'Butter'),
    ('Toast', 'Toast'),
    ('Smoke', 'Smoke'),
)

FLAVOUR = (
    ('Sweet', 'Sweet'),
    ('Sour', 'Sour'),
    ('Salt', 'Salt'),
    ('Delicate', 'Delicate'),
    ('Rich', 'Rich'),
    ('Intense', 'Intense'),
    ('Pungent', 'Pungent'),
    ('Musty', 'Musty'),
    ('Pest-Crop', 'Pest-Crop'),
    ('Woody', 'Woody'),
    ('Flat', 'Flat'),
    ('Greenish', 'Greenish'),
    ('Fruity', 'Fruity'),
    ('Balanced', 'Balanced'),
    ('Exotic', 'Exotic'),
    ('Chocolate', 'Chocolate'),
    ('Spicy', 'Spicy'),
    ('Nutty', 'Nutty'),
)

TEXTURE = (
    ('Buttery','Buttery'),
    ('Creamy','Creamy'),
    ('Smooth','Smooth'),
    ('Rich','Rich'),
    ('Velvety','Velvety'),
    ('Watery','Watery'),
    ('Oily','Oily'),
    ('Dry','Dry'),
    ('Chalky','Chalky'),
    ('Gritty','Gritty'),
    ('Rough','Rough'),
    ('Astringent','Astringent'),
    ('Metallic','Metallic'),
)

FINISH = (
    ('Short','Short'),
    ('Dry','Dry'),
    ('Bitter','Bitter'),
    ('Sour','Sour'),
    ('Harsh','Harsh'),
    ('Dirty','Dirty'),
    ('Clean','Clean'),
    ('Floral','Floral'),
    ('Fruity','Fruity'),
    ('Lingering','Lingering'),
    ('Resonant','Resonant'),
)

GENERAL = (
    ("Low", "Low"),
    ("Low-Medium", "Low-Medium"),
    ("Medium", "Medium"),
    ("Medium-High", "Medium-High"),
    ("High", "High"),
)
METHOD = (
    ("Batch", "Batch"),
    ("v60", "v60"),
)

# Create your models here.
class User(AbstractUser):
    pass

class Coffee(models.Model):
    CATEGORIES = (
        ("1","Rituals"),
        ("2","Ventures"),
        ("3","Horizons"),
    )
    name = models.CharField(max_length=60)
    origin = models.CharField(max_length=60)
    cultivar = models.CharField(max_length=60, default="cultivar_1")
    process = models.CharField(max_length=60)
    roast_profile = models.CharField(max_length=20)
    taste_profile = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=20, choices=CATEGORIES, default="1")
    traceability = models.CharField(max_length=60)
    is_house = models.BooleanField(default=True)
    is_guest = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}: {self.origin}, {self.process}, {self.roast_profile}, {self.display_category()}"

    def display_category(self):
        return str(self.get_category_display())



class Espresso(models.Model):
    coffee_name = models.ForeignKey(Coffee, on_delete=models.CASCADE, related_name="coffee_name", limit_choices_to={"roast_profile": "Espresso"})
    timestamp = models.DateTimeField(auto_now_add=True)
    water_temp = models.DecimalField(max_digits=3, decimal_places=1)
    water_tds = models.DecimalField(max_digits=3, decimal_places=2)
    batch_number = models.CharField(max_length=8)
    dry_weight = models.DecimalField(max_digits=3, decimal_places=1, default=18.0)
    wet_weight = models.IntegerField(default=36)
    extraction_time = models.CharField(max_length=10, default="26-28")
    acidity_score = models.FloatField(validators=[MinValueValidator(6), MaxValueValidator(10)])
    acidity_quality = models.CharField(max_length= 15,choices=ACIDITY, default = "Delicate")
    aroma = models.CharField(max_length=15, choices=AROMAS, default="Berry")
    flavour_score = models.FloatField(validators=[MinValueValidator(6), MaxValueValidator(10)])
    flavour_quality = models.CharField(max_length=15, choices = FLAVOUR, default="Sweet")
    texture = models.CharField(max_length=15, choices = GENERAL, default="Medium")
    texture_quality = models.CharField(max_length=15, choices=TEXTURE, default="Velvety")
    balance = models.CharField(max_length=15, choices=GENERAL, default="Medium")
    sweetness = models.CharField(max_length=15, choices=GENERAL, default="Medium")
    bitterness = models.CharField(max_length=15, choices=GENERAL, default="Medium")
    body = models.CharField(max_length=15, choices=GENERAL, default="Medium")
    finish = models.CharField(max_length=15, choices=FINISH, default="Lingering")
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Log: {self.id} added on {self.timestamp.strftime('%d %B %Y %H:%M')}"

class Filter(models.Model):
    coffee_name = models.ForeignKey(Coffee, on_delete=models.CASCADE, related_name="filter_coffee_name", limit_choices_to={"roast_profile": "Filter"})
    batch_number = models.CharField(max_length = 8)
    method = models.CharField(max_length=5, choices=METHOD, default="Batch")
    timestamp = models.DateTimeField(auto_now_add=True)
    water_temperature = models.DecimalField(max_digits=2, decimal_places=0)
    water_tds = models.DecimalField(max_digits=3, decimal_places=1)
    grind_size = models.DecimalField(max_digits=3, decimal_places=1)
    recipe = models.TextField()
    acidity_score = models.FloatField(validators=[MinValueValidator(6), MaxValueValidator(10)])
    acidity_quality = models.CharField(max_length= 15,choices=ACIDITY, default = "Delicate")
    aroma = models.CharField(max_length=15, choices=AROMAS, default="Berry")
    flavour_score = models.FloatField(validators=[MinValueValidator(6), MaxValueValidator(10)])
    flavour_quality = models.CharField(max_length=15, choices = FLAVOUR, default="Sweet")
    texture = models.CharField(max_length=15, choices = GENERAL, default="Medium")
    texture_quality = models.CharField(max_length=15, choices=TEXTURE, default="Velvety")
    balance = models.CharField(max_length=15, choices=GENERAL, default="Medium")
    sweetness = models.CharField(max_length=15, choices=GENERAL, default="Medium")
    bitterness = models.CharField(max_length=15, choices=GENERAL, default="Medium")
    body = models.CharField(max_length=15, choices=GENERAL, default="Medium")
    finish = models.CharField(max_length=15, choices=FINISH, default="Lingering")
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Log: {self.id} added on {self.timestamp.strftime('%d %B %Y %H:%M')}"



