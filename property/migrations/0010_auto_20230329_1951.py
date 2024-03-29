# Generated by Django 2.2.24 on 2023-03-29 16:51

from django.db import migrations


def get_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flat_set = Flat.objects.all()
    Owner = apps.get_model('property', 'Owner')
    for flat in flat_set.iterator():
        Owner.objects.get_or_create(owner=flat.owner,
                                    owners_phonenumber=flat.owners_phonenumber,
                                    owner_pure_phone=flat.owner_pure_phone)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20230329_1947'),
    ]

    operations = [migrations.RunPython(get_owner),
    ]
