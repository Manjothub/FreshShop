# Generated by Django 4.0.4 on 2022-05-29 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250)),
                ('product_quantity', models.IntegerField()),
                ('product_stock_availability', models.IntegerField()),
                ('product_description', models.TextField()),
                ('product_price', models.IntegerField()),
                ('product_images', models.ImageField(upload_to='media/product-images/')),
                ('product_status', models.BooleanField(default=False)),
            ],
        ),
    ]
