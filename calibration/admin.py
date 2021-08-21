from django.contrib import admin
from .models import User, Coffee, Espresso

# Register your models here.
admin.site.register(User)
admin.site.register(Coffee)
admin.site.register(Espresso)
