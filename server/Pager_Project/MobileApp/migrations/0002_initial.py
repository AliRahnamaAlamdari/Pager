# Generated by Django 3.2.7 on 2021-09-24 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RestaurantApp', '0001_initial'),
        ('MobileApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='Restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='RestaurantApp.restaurant'),
        ),
        migrations.AddField(
            model_name='orders',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='Food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RestaurantApp.fooditem'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='Order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='MobileApp.orders'),
        ),
    ]
