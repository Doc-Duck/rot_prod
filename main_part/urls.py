from django.urls import path
from .views import *


urlpatterns = [
    path('doctor_page/', doctor_page, name='doctor_page'),
    path('<int:id>', detail_view, name='patient_page')
]