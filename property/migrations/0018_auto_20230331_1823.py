# Generated by Django 2.2.24 on 2023-03-31 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20230330_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(db_index=True, related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
