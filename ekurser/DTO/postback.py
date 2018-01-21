
class Postback(object):

    def __init__(self, ispostback=True, success=True, message=None):
        self.ispostback = ispostback
        self.success = success
        self.message = message or ''
