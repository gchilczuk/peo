from django.db import models, Error
from .users import NauczycielAkademicki, Student


class GrupaZajeciowa(models.Model):
    czyuruchomiona = models.BooleanField()
    liczbamiejsc = models.IntegerField()
    liczbauczestnikow = models.IntegerField()
    rodzajgrupy = models.ForeignKey('Rodzajgrupy', models.DO_NOTHING, blank=True, null=True)
    termin = models.ForeignKey('Termin', models.DO_NOTHING, related_name='zajecia')
    kurs = models.ForeignKey('Kurs', models.DO_NOTHING, related_name='grupa')
    organizator = models.ForeignKey('Student', models.DO_NOTHING, related_name='grupa')
    prowadzacy = models.ManyToManyField('NauczycielAkademicki', related_name='grupa')
    student = models.ManyToManyField('Student', related_name='grupaZajeciowa')
    opinia = models.ManyToManyField('Opinia', related_name='grupa')

    def add_student(self, student: Student):
        """Add new Student to group."""
        if (self.liczbauczestnikow == self.liczbamiejsc):
            Error('There is already a maximum number of students.')
        pass  #

    def add_prowadzacy(self, prowadzacy: NauczycielAkademicki):
        """Add new teacher to group."""
        if (self.prowadzacy.count() == 2):
            Error('There is already a maximum number of teachers.')
        pass  #

    def add_opinia(self):
        pass


class Kurs(models.Model):
    wartoscgodzinowa = models.IntegerField()
    ects = models.IntegerField()
    nazwakursu = models.CharField(max_length=255)
    zamiennik = models.ManyToManyField('self', related_name='kurs', symmetrical=True)
    opiekun = models.ManyToManyField('NauczycielAkademicki', related_name='kurs')
    prowadzacy = models.ManyToManyField('NauczycielAkademicki', related_name='kwalifikowaneKursy')

    def add_opiekun(self, opiekun: NauczycielAkademicki):
        if (self.opiekun.count() == 2):
            Error('There is already a maximum number of tutors.')
        pass


class Opinia(models.Model):
    opiekun = models.ForeignKey('NauczycielAkademicki', models.DO_NOTHING)
    tresc = models.CharField(max_length=2500)


class Termin(models.Model):
    dzien = models.ForeignKey('DzienTygodnia', models.DO_NOTHING)
    godzina = models.CharField(max_length=10)
    sala = models.CharField(max_length=10)


class WniosekOUruchomienieGrupyZajeciowej(models.Model):
    student = models.ForeignKey('Student', models.DO_NOTHING)
    zgodapelnomocnika = models.NullBooleanField()
    statuswniosku = models.ForeignKey('StatusWniosku', models.DO_NOTHING, blank=True, null=True)
    nrwniosku = models.CharField(max_length=10)
