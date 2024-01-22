# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError

from pizza.models import PizzaOrder, Address

__author__ = 'sobolevn'


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'full',
        ]


class PizzaOrderForm(forms.ModelForm):
    class Meta:
        model = PizzaOrder
        exclude = [
            'delivered',
            'date_created',
            'date_delivered',
            'delivery',
        ]

    def clean(self):
        data = self.cleaned_data
        excluded = data['exclude']

        errors = []
        for item in excluded:
            if item in data['extra']:
                errors.append(unicode(item))

        if errors:
            raise ValidationError(
                'Ingredients [{}] are in extras and excludes!'.format(
                    ', '.join(errors)
                )
            )
        return data

    def save(self, commit=True, delivery=None):
        if delivery is None:
            raise ValueError('Delivery was not set')

        inst = super(PizzaOrderForm, self).save(commit=False)
        inst.delivery = delivery
        if commit:
            inst.save()

        return inst
