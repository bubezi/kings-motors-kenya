# Generated by Django 3.2 on 2021-05-01 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_product_image_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='descriprion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]