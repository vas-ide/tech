from django.template.defaulttags import url
from django.urls import path
from . import views
from .views import Shift

urlpatterns = [
    path('', views.index),
    # path('shift/', views.shift),
    path('shift/', Shift.as_view(), name='shift'),

]
