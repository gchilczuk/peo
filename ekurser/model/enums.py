from django.db import models


class DzienTygodnia(models.Model):
    nazwa = models.CharField(max_length=32)


class RodzajGrupy(models.Model):
    nazwa = models.CharField(max_length=32)


class StatusWniosku(models.Model):
    nazwa = models.CharField(max_length=32)
