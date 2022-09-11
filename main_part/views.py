import random
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from .models import *


def doctor_page(request):
    #for i in range(10):
     #   Measurements(hemoglobin=random.randint(10,20), oxygination=random.randint(10,20), datetime=datetime.datetime.now(), patient_id=1).save()
    patients = Measurements.objects.all().order_by('hemoglobin')
    for pt in patients:
        print(pt.datetime.date())
    return render(request, 'main_part/doctor_page.html', context={'patient': patients})


def detail_view(request, id):
    measurement = Measurements.objects.get(id=id)
    patients = Measurements.objects.all().order_by('hemoglobin')
    return render(request, 'main_part/detail_view.html', context={'measure': measurement, 'patient': patients})

