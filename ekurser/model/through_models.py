from django.db import models


class Prowadzenie(models.Model):
    grupa = models.ForeignKey('GrupaZajeciowa', models.DO_NOTHING, db_column='grupazajeciowaid')
    prowadzacy = models.ForeignKey('NauczycielAkademicki', models.DO_NOTHING, db_column='nauczycielakademickiid')

    class Meta:
        managed = False
        db_table = 'grupazajeciowa_nauczycielakademicki'
        unique_together = ('grupa', 'prowadzacy')


class KursKurs(models.Model):
    kurs = models.ForeignKey('Kurs', models.DO_NOTHING, db_column='kursid', related_name='zamienniki')
    zamiennik = models.ForeignKey('Kurs', models.DO_NOTHING, db_column='kursid2', related_name='kursy')

    class Meta:
        managed = False
        db_table = 'kurs_kurs'
        unique_together = ('kurs', 'zamiennik')


class Opieka(models.Model):
    kurs = models.ForeignKey('Kurs', models.DO_NOTHING, db_column='kursid')
    nauczycielakademicki = models.ForeignKey('NauczycielAkademicki', models.DO_NOTHING,
                                             db_column='nauczycielakademickiid')

    class Meta:
        managed = False
        db_table = 'nauczycielakademicki_kurs'
        unique_together = ('kurs', 'nauczycielakademicki')


class Kwalifikacje(models.Model):
    nauczycielakademicki = models.ForeignKey('NauczycielAkademicki', models.DO_NOTHING,
                                             db_column='nauczycielakademickiid')
    kurs = models.ForeignKey('Kurs', models.DO_NOTHING, db_column='kursid')

    class Meta:
        managed = False
        db_table = 'nauczycielakademicki_kurs2'
        unique_together = ('nauczycielakademicki', 'kurs')


class Uczestnictwo(models.Model):
    grupazajeciowa = models.ForeignKey('GrupaZajeciowa', models.DO_NOTHING, db_column='grupazajeciowaid')
    student = models.ForeignKey('Student', models.DO_NOTHING, db_column='studentid')

    class Meta:
        managed = False
        db_table = 'student_grupazajeciowa'
        unique_together = ('grupazajeciowa', 'student')
