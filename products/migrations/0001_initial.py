# Generated by Django 5.1.7 on 2025-03-25 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('electronics', 'Electronics'), ('fashion', 'Fashion'), ('home_appliances', 'Home Appliances'), ('books', 'Books'), ('beauty', 'Beauty & Personal Care'), ('sports', 'Sports & Fitness'), ('toys', 'Toys & Games')], max_length=50)),
                ('images', models.ImageField(blank=True, null=True, upload_to='product_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_level', models.PositiveIntegerField(default=0)),
                ('seller', models.ForeignKey(limit_choices_to={'role': 'Seller'}, on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
