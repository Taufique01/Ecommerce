# Generated by Django 2.2 on 2020-03-09 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_item_common_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('fruits', 'Fruits'), ('crops', 'Crops'), ('vegetable', 'Vegetable')], max_length=2),
        ),
    ]
