from django.core.checks import messages
from django.shortcuts import render
from django.views import View
from .models import Employee, Shift, ShiftDay

from staff.forms import ShiftForm


def index(request):
    content = {}
    return render(request, 'staff/index.html', content)

class Shifts(View):
    def get(self, request):

        context = {
            # "employee": Employee.objects.all(),
            "shift": Shift.objects.all(),
            # "shiftday": ShiftDay.objects.all(),

        }
        return render(request, 'staff/shifts.html', context)
    def post(self, request):
        context = {}
        return render(request, 'staff/shifts.html', context)

class Employees(View):
    def get(self, request):
        context = {}
        return render(request, 'staff/employees.html', context)

    def post(self, request):
        context = {}
        return render(request, 'staff/employees.html', context)
class Menagement(View):
    def get(self, request):
        context = {}
        return render(request, 'staff/menagement.html', context)
    def post(self, request):
        context = {}
        return render(request, 'staff/menagement.html', context)



class StandartMessages(View):
    def get(self, request):

        form = ShiftForm()
        context = {
            'form': form,
        }
        return render(request, 'staff/standart_messages.html', context)
    def post(self, request):

        form = ShiftForm(data=request.POST)
        if form.is_valid():
            messages.success(request, form.cleaned_data['messages'])
        else:
            messages.error(request, f'Validation failed')
        context = {
            'form': form,
        }
        return render(request, 'staff/standart_messages.html', context)