# Generated by Django 5.1.1 on 2024-09-28 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vysota', '0005_alter_company_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(max_length=300),
        ),
        migrations.DeleteModel(
            name='Checkout',
        ),
    ]
