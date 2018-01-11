from django.db import models
from django.contrib.auth.models import User

class Dzientygodnia(models.Model):
    nazwa = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'dzientygodnia'


class Grupazajeciowa(models.Model):
    kursid = models.ForeignKey('Kurs', models.DO_NOTHING, db_column='kursid')
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='studentid')
    rodzajgrupy = models.ForeignKey('Rodzajgrupy', models.DO_NOTHING, db_column='rodzajgrupy', blank=True, null=True)
    czyuruchomiona = models.BooleanField()
    liczbamiejsc = models.IntegerField()
    liczbauczestnikow = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'grupazajeciowa'


class GrupazajeciowaNauczycielakademicki(models.Model):
    grupazajeciowaid = models.ForeignKey(Grupazajeciowa, models.DO_NOTHING, db_column='grupazajeciowaid', primary_key=True)
    nauczycielakademickiid = models.ForeignKey('Nauczycielakademicki', models.DO_NOTHING, db_column='nauczycielakademickiid')

    class Meta:
        managed = False
        db_table = 'grupazajeciowa_nauczycielakademicki'
        unique_together = (('grupazajeciowaid', 'nauczycielakademickiid'),)


class Kurs(models.Model):
    wartoscgodzinowa = models.IntegerField()
    ects = models.IntegerField()
    nazwakursu = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'kurs'


class KursKurs(models.Model):
    kursid = models.ForeignKey(Kurs, models.DO_NOTHING, db_column='kursid', primary_key=True)
    kursid2 = models.ForeignKey(Kurs, models.DO_NOTHING, db_column='kursid2')

    class Meta:
        managed = False
        db_table = 'kurs_kurs'
        unique_together = (('kursid', 'kursid2'),)



class NauczycielakademickiKurs(models.Model):
    nauczycielakademickiid = models.ForeignKey(Nauczycielakademicki, models.DO_NOTHING, db_column='nauczycielakademickiid', primary_key=True)
    kursid = models.ForeignKey(Kurs, models.DO_NOTHING, db_column='kursid')

    class Meta:
        managed = False
        db_table = 'nauczycielakademicki_kurs'
        unique_together = (('nauczycielakademickiid', 'kursid'),)


class NauczycielakademickiKurs2(models.Model):
    nauczycielakademickiid = models.ForeignKey(Nauczycielakademicki, models.DO_NOTHING, db_column='nauczycielakademickiid', primary_key=True)
    kursid = models.ForeignKey(Kurs, models.DO_NOTHING, db_column='kursid')

    class Meta:
        managed = False
        db_table = 'nauczycielakademicki_kurs2'
        unique_together = (('nauczycielakademickiid', 'kursid'),)


class Opinia(models.Model):
    grupazajeciowaid = models.ForeignKey(Grupazajeciowa, models.DO_NOTHING, db_column='grupazajeciowaid')
    nauczycielakademickiid = models.ForeignKey(Nauczycielakademicki, models.DO_NOTHING, db_column='nauczycielakademickiid')
    tresc = models.CharField(max_length=2500)

    class Meta:
        managed = False
        db_table = 'opinia'


class Rodzajgrupy(models.Model):
    nazwa = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'rodzajgrupy'


class Statuswniosku(models.Model):
    nazwa = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'statuswniosku'


class StudentGrupazajeciowa(models.Model):
    studentid = models.ForeignKey(Student, models.DO_NOTHING, db_column='studentid', primary_key=True)
    grupazajeciowaid = models.ForeignKey(Grupazajeciowa, models.DO_NOTHING, db_column='grupazajeciowaid')

    class Meta:
        managed = False
        db_table = 'student_grupazajeciowa'
        unique_together = (('studentid', 'grupazajeciowaid'),)


class Termin(models.Model):
    grupazajeciowaid = models.ForeignKey(Grupazajeciowa, models.DO_NOTHING, db_column='grupazajeciowaid', blank=True, null=True)
    dzien = models.ForeignKey(Dzientygodnia, models.DO_NOTHING, db_column='dzien', blank=True, null=True)
    godzina = models.CharField(max_length=10, blank=True, null=True)
    sala = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'termin'


class Wniosekouruchomieniegrupyzajeciowej(models.Model):
    studentid = models.ForeignKey(Student, models.DO_NOTHING, db_column='studentid')
    zgodapelnomocnika = models.NullBooleanField()
    statuswniosku = models.ForeignKey(Statuswniosku, models.DO_NOTHING, db_column='statuswniosku', blank=True, null=True)
    nrwniosku = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wniosekouruchomieniegrupyzajeciowej'
