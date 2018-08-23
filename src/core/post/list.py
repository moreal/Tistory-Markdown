from core import Tima
from typing import List


def _list(tima: Tima) -> List:
    import json
    json.loads(tima.pytistory.post.list(
        blog_name=tiam.blog_name
    ))
    
    # return list(map(tima.pytistory.post.list(tima.blog_name)))
