# Generated by Django 3.1.5 on 2021-10-20 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products_api', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='deliveryTime',
            field=models.TimeField(default=1634761344.3864613),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='orederTime',
            field=models.TimeField(default=1634757744.3864613),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_api.productmodel'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]