# Generated by Django 4.2.7 on 2023-11-22 15:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0011_alter_statusemployee_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shiftday',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
