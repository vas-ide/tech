from django.core.checks import messages
from django.shortcuts import render
from django.views import View

from shift.forms import ShiftForm


def index(request):
    content = {}
    return render(request, 'shift/index.html', content)


# def shift(request):
#     content = {}
#     return render(request, 'shift/shift.html', content)



class Shift(View):
    def get(self, request):

        form = ShiftForm()
        context = {
            'form': form,
        }
        return render(request, 'shift/shift.html', context)
    def post(self, request):

        form = ShiftForm(data=request.POST)
        if form.is_valid():
            messages.success(request, form.cleaned_data['messages'])
        else:
            messages.error(request, f'Validation failed')
        context = {
            'form': form,
        }
        return render(request, 'shift/shift.html', context)