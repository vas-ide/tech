from django.db import models


# Create your models here.


class Employee(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True, db_index=True)
    surname = models.CharField(max_length=150, blank=False, null=False)
    name = models.CharField(max_length=150, blank=False, null=False)
    lastname = models.CharField(max_length=150, blank=False, null=False)
    active = models.BooleanField(default=True, blank=False, null=False)

    def __str__(self):
        return f"{self.surname} {self.name} {self.lastname} - №{self.id}"


class Shift(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True, db_index=True)

    def __str__(self):
        return f"Shift № {self.id}"


class StandartShift(models.Model):
    number = models.ForeignKey("Shift", on_delete=models.PROTECT)
    employee = models.ForeignKey("Employee", on_delete=models.PROTECT)
    status = models.ForeignKey("StatusEmployee", on_delete=models.PROTECT, related_name="status_emp")

    def __str__(self):
        return f"Shift № {self.number}"


class ShiftDay(models.Model):
    number = models.ForeignKey('Shift', on_delete=models.PROTECT)
    date = models.DateField(null=False, blank=False)

    def __str__(self):
        return f"{self.date} {self.number}"


class StatusEmployee(models.Model):
    EDUCATION = ("ED", "Education")
    SICK = ("SI", "Sick")
    VACATION = ("VA", "Vacation")
    DAY_OFF = ("DO", "Day off")
    TIME_OFF = ("TO", "Time off")
    ON_THE_JOB = ("OJ", "On the job")
    ABSENTEEISM = ("AB", "Absenteeism")
    __all = (EDUCATION, SICK, VACATION, DAY_OFF, TIME_OFF, ON_THE_JOB, ABSENTEEISM)
    choice = models.CharField(max_length=2, choices=__all, unique=True, default="OJ")

    def __str__(self):
        return f"{self.choice}"
