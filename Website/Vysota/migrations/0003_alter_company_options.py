# Generated by Django 5.1.1 on 2024-09-28 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vysota', '0002_company_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['id'], 'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
    ]
