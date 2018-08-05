from core import Tima


class Post():
    def __init__(self, tima: Tima):
        self.tima = tima

        from core.post.upload import _upload
        self.upload = _upload

        from core.post.create import _create
        self.create = _create

        from core.post.list import _list
        self.list = _list
