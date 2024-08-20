# Generated by Django 5.1 on 2024-08-20 08:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0008_equipment_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equip', to='equipment.category'),
        ),
    ]
