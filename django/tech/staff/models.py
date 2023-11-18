from django.db import models


# Create your models here.


class Employee(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, db_index=True)
    surname = models.CharField(max_length=150, blank=False, null=False, )
    name = models.CharField(max_length=150, blank=False, null=False, )
    lastname = models.CharField(max_length=150, blank=False, null=False, )

    def __str__(self):
        return f"{self.surname} {self.name} {self.lastname} - №{self.id}"


class Shift(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True, db_index=True)

    def __str__(self):
        return f"Shift № {self.id}"


class ShiftDay(models.Model):
    number = models.ForeignKey('Shift', on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    employee = models.ManyToManyField('Employee', related_name='employees')
    # employee = models.ForeignKey('Employee', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} {self.number} {self.employee}"
