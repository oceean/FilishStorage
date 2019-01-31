# TODO Sweet exceptions

class FilishException(Exception):
    pass

class FilishKeyError(FilishException):
    pass

class FilishDamagedItem(FilishException):
    pass