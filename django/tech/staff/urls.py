from django.template.defaulttags import url
from django.urls import path
from . import views
from .views import Shifts, Employees, Menagement, StandartMessages

urlpatterns = [
    path('', views.index),
    # path('staff/', views.staff),
    path('shifts/', Shifts.as_view(), name='shifts'),
    path('employees/', Employees.as_view(), name='employees'),
    path('menagement/', Menagement.as_view(), name='menagement'),
    path('standart_messages/', StandartMessages.as_view(), name='standart_messages'),


]
