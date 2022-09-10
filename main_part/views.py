import random

from django.shortcuts import render
from .models import *


def doctor_page(request):
    #for i in range(10):
     #   Measurements(hemoglobin=random.randint(10,20), oxygination=random.randint(10,20), datetime=datetime.datetime.now(), patient_id=1).save()
    patients = Measurements.objects.all().order_by('hemoglobin')
    for pt in patients:
        print(pt.datetime.date())
    return render(request, 'main_part/doctor_page.html', context={'patient': patients})


def patient_page(request):
    pass
