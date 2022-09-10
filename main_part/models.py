from django.db import models
import datetime
import django


class Patient(models.Model):
    name = models.CharField(max_length=150)
    age = models.CharField(max_length=150)
    sex = models.BooleanField()


class Measurements(models.Model):
    hemoglobin = models.CharField(max_length=150)
    oxygination = models.CharField(max_length=150)
    datetime = models.DateTimeField(default=django.utils.timezone.now)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)