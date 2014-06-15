
class GenericBoard(object):
    NAME = "Generic board"

    @classmethod
    def instantiate(cls, *args):
        return cls(*args)

