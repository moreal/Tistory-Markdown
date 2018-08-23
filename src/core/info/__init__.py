from pytistory import PyTistory
from config import VERSION


class Info():
    def __init__(self):
        from core.info.version import _version
        self.version = _version
