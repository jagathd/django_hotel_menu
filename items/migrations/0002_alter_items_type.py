# Generated by Django 4.1.7 on 2024-02-02 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='type',
            field=models.IntegerField(choices=[(0, 'Veg'), (1, 'Non-Veg')], default=0),
        ),
    ]
