from pytistory import PyTistory


class Post():
    def __init__(self):
        from core.post.upload import _upload
        self.upload = _upload

        from core.post.create import _create
        self.create = _create

        from core.post.list import _list
        self.list = _list
