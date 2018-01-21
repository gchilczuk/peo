from ekurser.model.models import *
from ekurser.model.through_models import *

def kreator_studenta():
    s1 = Student(
        imie='Jaś',
        nazwisko='Fasola',
        login='s228100',
        haslo='123qwe',
        nrindeksu='228100'
    )
    s2 = Student(
        imie='Paweł',
        nazwisko='Nowak',
        login='s228101',
        haslo='1234qwer',
        nrindeksu='228101'
    )
    s1.save()
    s2.save()

def nauczyciel_kreator():
    n1 = NauczycielAkademicki(
        imie='Jan',
        nazwisko='Groch',
        login='jan.groch',
        haslo='wszystkichstudentow',
        liczbagodzin=0,
        pensum=0,
        jestpelnomocnikiem=True
    )
    n2 = NauczycielAkademicki(
        imie='Stanisław',
        nazwisko='Pawlacz',
        login='stanislaw.pawlacz',
        haslo='wartoprobowac',
        liczbagodzin=0,
        pensum=0,
        jestpelnomocnikiem=False
    )
    n1.save()
    n2.save()

def kurs_kreator():
    k1 = Kurs(
        wartoscgodzinowa=1,
        ects=2,
        nazwakursu='Metody Systemowe i Decyzyjne')
    k2 = Kurs(
        wartoscgodzinowa=2,
        ects=3,
        nazwakursu='Projektowanie Oprogramowania')
    k3 = Kurs(
        wartoscgodzinowa=4,
        ects=5,
        nazwakursu='Paradygmaty Programowania')
    k1.save()
    k2.save()
    k3.save()

def termin_kreator():
    t1 = Termin(dzien_id=1, godzina='7:30', sala='127b/D2')
    t2 = Termin(dzien_id=2, godzina='9:15', sala='127c/D2')
    t3 = Termin(dzien_id=2, godzina='11:15', sala='127c/D2')
    t1.save()
    t2.save()
    t3.save()


def kreator_3():
    n1 = NauczycielAkademicki(
        imie='Benedykt',
        nazwisko='Gierosławski',
        login='benedykt.gieroslawski',
        haslo='robisie',
        liczbagodzin=0,
        pensum=0,
        jestpelnomocnikiem=False
    )
    n2 = NauczycielAkademicki(
        imie='Stanisław',
        nazwisko='Wokulski',
        login='stanislaw.wokulski',
        haslo='niewarto',
        liczbagodzin=0,
        pensum=0,
        jestpelnomocnikiem=False
    )
    n1.save()
    n2.save()
    k1 = Kwalifikacje(nauczycielakademicki=n1, kurs_id=3)
    k2 = Kwalifikacje(nauczycielakademicki=n2, kurs_id=2)
    k1.save()
    k2.save()
    o = Opieka(kurs_id=2, nauczycielakademicki=n2)
    o.save()


    s1 = Student(
        imie='Izabela',
        nazwisko='Łęcka',
        login='s228102',
        haslo='12345678',
        nrindeksu='228102'
    )
    s1.save()

    gr1 = GrupaZajeciowa(
        kurs_id=3,
        organizator=s1,
        rodzajgrupy_id=1,
        czyuruchomiona=False,
        liczbamiejsc=15,
        liczbauczestnikow=0
    )
    gr2 = GrupaZajeciowa(
        kurs_id=3,
        organizator_id=2,
        rodzajgrupy_id=2,
        czyuruchomiona=False,
        liczbamiejsc=15,
        liczbauczestnikow=0
    )
    gr3 = GrupaZajeciowa(
        kurs_id=1,
        organizator_id=2,
        rodzajgrupy_id=2,
        czyuruchomiona=False,
        liczbamiejsc=15,
        liczbauczestnikow=0
    )

    gr1.save()
    gr2.save()
    gr3.save()


    p1 = Prowadzenie(prowadzacy=n1, grupa=gr1)
    p2 = Prowadzenie(prowadzacy_id=2, grupa_id=2)
    p1.save()
    p2.save()


def wniosek_kreator():
    w1 = WniosekOUruchomienieGrupyZajeciowej(
        student_id=3,
        statuswniosku_id=1,
        nrwniosku=12018,
        grupazajeciowa_id=3
    )
    w2 = WniosekOUruchomienieGrupyZajeciowej(
        student_id=2,
        statuswniosku_id=1,
        nrwniosku=22018,
        grupazajeciowa_id=3
    )
    w1.save()
    w2.save()