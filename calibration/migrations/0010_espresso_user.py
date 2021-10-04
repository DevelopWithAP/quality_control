# Generated by Django 3.1.7 on 2021-09-13 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calibration', '0009_auto_20210825_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='espresso',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='log_site', to=settings.AUTH_USER_MODEL),
        ),
    ]