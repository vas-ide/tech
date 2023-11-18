from django.contrib import admin
from .models import Employee, Shift, ShiftDay


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "surname", "name", "lastname"]


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(ShiftDay)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ["number", "date"]
