"""DTO do zastosowania w widokach pracownika"""

class Wniosek(object):
    """Reprezentacja wniosku o uruchomienie grupy"""

    def __init__(self, numer, status, kurs, skladajacy, prowadzacy, zapisanych, rodzaj, sala, termin, opinia, zgoda=None,id=None):
        self.numer = numer
        self.status = status
        self.kurs = kurs
        self.skladajacy = skladajacy
        self.prowadzacy = prowadzacy
        self.zapisanych = zapisanych
        self.rodzaj = rodzaj
        self.sala = sala
        self.termin = termin
        self.opinia = opinia
        self.zgoda = zgoda or "Brak informacji"
        self.id = id
