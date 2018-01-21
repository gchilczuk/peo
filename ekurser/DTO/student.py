from collections import namedtuple

Location = namedtuple('Location', ['name', 'href'])


class Navigation(object):

    def __init__(self, user, location,  **kwargs):
        self.user = user
        self.location = location
        self.other = kwargs

    def __getitem__(self, name: str):
        item = self.other.get(name, None)
        if item is None:
            item = self.__getattribute__(name)
        return item

class Group(object):

    def __init__(self, kurs, prowadzacy, rodzaj, sala, termin, zapisanych, miejsc, id):
        self.kurs = kurs
        self.prowadzacy = prowadzacy
        self.rodzaj = rodzaj
        self.sala = sala
        self.termin = termin
        self.zapisanych = zapisanych
        self.miejsc = miejsc
        self.id = id


