# Generated by Django 4.2.7 on 2023-11-17 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_alter_shift_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shiftday',
            name='date',
            field=models.DateField(),
        ),
    ]
