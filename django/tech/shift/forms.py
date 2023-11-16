import datetime

from django import forms
from django.core.exceptions import ValidationError


class ShiftForm(forms.Form):
    date = forms.DateField()
    position = forms.CharField(max_length=100)
    difficultys = forms.FloatField()
    description = forms.CharField(max_length=1000)


    def clean_position(self):
        position = self.cleaned_data['position']
        if len(position) < 5:
            raise ValidationError(f'Unknown working position!')
        return position
    #
    def clean_difficultys(self):
        pass
