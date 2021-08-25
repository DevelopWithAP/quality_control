# Generated by Django 3.1.7 on 2021-08-25 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calibration', '0006_auto_20210825_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espresso',
            name='coffee_name',
            field=models.ForeignKey(limit_choices_to={'roast_profile': 'Espresso'}, on_delete=django.db.models.deletion.CASCADE, related_name='coffee_name', to='calibration.coffee'),
        ),
    ]
