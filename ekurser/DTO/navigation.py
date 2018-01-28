"""DTO ogólnego zastosowania"""

from collections import namedtuple

Location = namedtuple('Location', ['name', 'href'])


class Navigation(object):
    """
    Podstawowy obiekt przekazujący dane o zalogowanym użytkowniku i możliwościach nawigacji
    """

    def __init__(self, user, location, uid=1, permissions=None, **kwargs):
        """
        Inicjacja DTO nawigacji

        :param user: nazwa aktualnie zalogowanego użytkownika
        :param location: ścieżka do bieżącego położenia
        :param uid: id użytkownika
        :param permissions: dodatkowe uprawnienia użytkownika
        :param kwargs: dowolne argumenty
        """
        self.user = user
        self.location = location
        self.uid = uid
        self.permissions = permissions or {}
        self.other = kwargs

    def __getitem__(self, name: str):
        item = self.other.get(name, None)
        if item is None:
            item = self.__getattribute__(name)
        return item


class Postback(object):
    """Reprezentacja obiektu kontrolnego formularzy zatwierdzanych samym sobie"""

    def __init__(self, ispostback=True, success=True, message=None):
        self.ispostback = ispostback
        self.success = success
        self.message = message or ''
