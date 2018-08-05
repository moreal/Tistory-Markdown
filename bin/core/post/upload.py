from core import Tima
from frontmatter import loads
from typing import AnyStr


def _upload(tima: Tima, filename: AnyStr):
    with open(filename, 'r') as f:
        content = f.read()

        pass
        # from core.post.util import get_category
        # tima.pytistory.post.write()
