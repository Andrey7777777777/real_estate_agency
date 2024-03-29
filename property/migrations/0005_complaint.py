# Generated by Django 2.2.24 on 2023-03-29 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0004_auto_20230329_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Текст жалобы')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to='property.Flat', verbose_name='Объект жалобы')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to=settings.AUTH_USER_MODEL, verbose_name='Жалоба от')),
            ],
        ),
    ]
