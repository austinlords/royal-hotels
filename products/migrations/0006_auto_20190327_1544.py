# Generated by Django 2.0.7 on 2019-03-27 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190327_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('entrees', 'entrees'), ('drinks', 'drinks'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]
