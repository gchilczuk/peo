from collections import namedtuple

Location = namedtuple('Location', ['name', 'href'])


class Navigation(object):

    def __init__(self, user, location, uid=1, **kwargs):
        self.user = user
        self.location = location
        self.uid = uid
        self.other = kwargs

    def __getitem__(self, name: str):
        item = self.other.get(name, None)
        if item is None:
            item = self.__getattribute__(name)
        return item


class Postback(object):

    def __init__(self, ispostback=True, success=True, message=None):
        self.ispostback = ispostback
        self.success = success
        self.message = message or ''
