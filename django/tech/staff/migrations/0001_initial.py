# Generated by Django 4.2.7 on 2023-11-17 pillow_ticket:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(db_index=True, primary_key=True, serialize=False, unique=True)),
                ('surname', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('lastname', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.IntegerField(db_index=True, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.employee')),
            ],
        ),
    ]
