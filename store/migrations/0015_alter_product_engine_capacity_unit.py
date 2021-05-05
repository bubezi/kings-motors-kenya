# Generated by Django 3.2 on 2021-05-05 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20210505_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='engine_capacity_unit',
            field=models.CharField(blank=True, choices=[('select', 'SELECT'), ('liter', 'LITERS'), ('cc', 'CC')], default='liters', max_length=10, null=True),
        ),
    ]
