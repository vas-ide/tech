from django.contrib import admin
from .models import Employee, Shift, StandartShift, ShiftDay, StatusEmployee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "surname", "name", "lastname"]


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(StandartShift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ["number", "employee"]


@admin.register(ShiftDay)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ["number", "date"]



@admin.register(StatusEmployee)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ["choice"]
