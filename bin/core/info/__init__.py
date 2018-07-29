from pytistory import PyTistory


class Info():
    def __init__(self, pytistory: PyTistory):
        self.pytistory = pytistory

    def version(self) -> dict:
        return self.pytistory.blog.info()