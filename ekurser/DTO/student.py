"""DTO do zastosowania w widokach studenta"""

class Group(object):
    """Reprezentacja tworzącej się grupy zajęciowej"""

    def __init__(self, kurs, prowadzacy, rodzaj, sala, termin, zapisanych, miejsc, uruchomiona, id):
        self.kurs = kurs
        self.prowadzacy = prowadzacy
        self.rodzaj = rodzaj
        self.sala = sala
        self.termin = termin
        self.zapisanych = zapisanych
        self.miejsc = miejsc
        self.uruchomiona = uruchomiona
        self.id = id
        self.zapisany = False



