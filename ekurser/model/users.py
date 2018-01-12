from django.db import models
from django.contrib.auth.models import User


class NauczycielAkademicki(User):
    imie = models.CharField(max_length=255)
    nazwisko = models.CharField(max_length=255)
    liczbagodzin = models.IntegerField()
    pensum = models.IntegerField()
    jestpelnomocnikiem = models.BooleanField()


class Student(User):
    imie = models.CharField(max_length=255)
    nazwisko = models.CharField(max_length=255)
    nrindeksu = models.CharField(unique=True, max_length=9)
