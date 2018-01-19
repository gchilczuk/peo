from django.db import models
from .enums import DzienTygodnia, RodzajGrupy, StatusWniosku


class MyUser(models.Model):
    imie = models.CharField(max_length=255)
    nazwisko = models.CharField(max_length=255)
    login = models.CharField(unique=True, max_length=30)
    haslo = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Student(MyUser):
    nrindeksu = models.CharField(unique=True, max_length=9)

    class Meta:
        managed = False
        db_table = 'student'


class NauczycielAkademicki(MyUser):
    liczbagodzin = models.IntegerField()
    pensum = models.IntegerField()
    jestpelnomocnikiem = models.BooleanField()
    kwalifikowaneKursy = models.ManyToManyField('Kurs', related_name='prowadzacy', through='Kwalifikacje',
                                                through_fields=('nauczycielakademicki', 'kurs'))

    class Meta:
        managed = False
        db_table = 'nauczycielakademicki'


class Kurs(models.Model):
    wartoscgodzinowa = models.IntegerField()
    ects = models.IntegerField()
    nazwakursu = models.CharField(max_length=255)
    zamiennik = models.ManyToManyField('self', related_name='kurs', through='KursKurs',
                                       through_fields=('kurs', 'zamiennik'), symmetrical=False)
    opiekun = models.ManyToManyField(NauczycielAkademicki, related_name='kursy',
                                     through='Opieka', through_fields=('kurs', 'nauczycielakademicki'))

    class Meta:
        managed = False
        db_table = 'kurs'


class GrupaZajeciowa(models.Model):
    kurs = models.ForeignKey(Kurs, models.DO_NOTHING, db_column='kursid')
    organizator = models.ForeignKey(Student, models.DO_NOTHING, db_column='studentid')
    rodzajgrupy = models.ForeignKey(RodzajGrupy, models.DO_NOTHING, db_column='rodzajgrupy')
    czyuruchomiona = models.BooleanField()
    liczbamiejsc = models.IntegerField()
    liczbauczestnikow = models.IntegerField()
    prowadzacy = models.ManyToManyField(NauczycielAkademicki, related_name='grupa',
                                        through='Prowadzenie',
                                        through_fields=('grupa', 'prowadzacy'))
    studenci = models.ManyToManyField(Student, related_name='grupaZajeciowa', through='Uczestnictwo',
                                      through_fields=('grupazajeciowa', 'student'))

    class Meta:
        managed = False
        db_table = 'grupazajeciowa'


class WniosekOUruchomienieGrupyZajeciowej(models.Model):
    student = models.ForeignKey(Student, models.DO_NOTHING, db_column='studentid')
    zgodapelnomocnika = models.NullBooleanField()
    statuswniosku = models.ForeignKey(StatusWniosku, models.DO_NOTHING, db_column='statuswniosku',
                                      blank=True, null=True)
    nrwniosku = models.IntegerField()
    grupazajeciowa = models.ForeignKey(GrupaZajeciowa, models.DO_NOTHING, db_column='grupazajeciowaid')

    class Meta:
        managed = False
        db_table = 'wniosekouruchomieniegrupyzajeciowej'


class Opinia(models.Model):
    grupazajeciowaid = models.ForeignKey(GrupaZajeciowa, models.DO_NOTHING, db_column='grupazajeciowaid')
    nauczycielakademickiid = models.ForeignKey(NauczycielAkademicki, models.DO_NOTHING,
                                               db_column='nauczycielakademickiid')
    tresc = models.CharField(max_length=2500)

    class Meta:
        managed = False
        db_table = 'opinia'


class Termin(models.Model):
    grupazajeciowaid = models.ForeignKey(GrupaZajeciowa, models.DO_NOTHING, db_column='grupazajeciowaid',
                                         blank=True, null=True)
    dzien = models.ForeignKey(DzienTygodnia, models.DO_NOTHING, db_column='dzien', blank=True, null=True)
    godzina = models.CharField(max_length=10, blank=True, null=True)
    sala = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'termin'