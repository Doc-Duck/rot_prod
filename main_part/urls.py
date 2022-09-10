from django.urls import path
from .views import *


urlpatterns = [
    path('doctor_page/', doctor_page, name='doctor_page'),
    path('patient_page/', patient_page, name='patient_page')
]