# Generated by Django 4.2.2 on 2023-06-06 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_shop_psc_alter_shop_street'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='shop',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cars.shop', verbose_name='Prodejna'),
        ),
    ]