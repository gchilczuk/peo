from django.db import models


class DzienTygodnia(models.Model):
    nazwa = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'dzientygodnia'


class RodzajGrupy(models.Model):
    nazwa = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'rodzajgrupy'


class StatusWniosku(models.Model):
    nazwa = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'statuswniosku'
