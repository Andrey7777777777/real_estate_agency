# Generated by Django 2.2.24 on 2023-03-29 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20230329_2039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owners_phonenumber',
            new_name='phonenumber',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_pure_phone',
            new_name='pure_phone',
        ),
    ]
