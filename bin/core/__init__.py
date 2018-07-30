from pytistory import PyTistory
from markdown2 import markdown

from core.post import Post
from core.info import Info


class Tima(object):
    def __init__(self):
        self.pytistory = PyTistory()
        self.post = Post(pytistory)
        self.info = Info(pytistory)

        from os import environ
        access_token = environ.get("TIMA_ACCESS_TOKEN")
        self.pytistory.configure(access_token=access_token)
        self.blog_name = environ.get("TIMA_BLOG_NAME")
