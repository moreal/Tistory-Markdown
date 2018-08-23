from core import Tima
from typing import List, AnyStr, Type


def is_type_list(_type: Type, _list: List[AnyStr]) -> bool:
    for el in _list:
        if type(el) != _type:
            return False
    return True


def get_category(_tima: Tima, _list: List[AnyStr]) -> int:
    if _list is None or len(_list) == 0:
        return -1

    resp = _tima.pytistory.category.list(blog_name=tima.blog_name)
    categories = data['tistory']['item']['categories']['category']

    _list = _list.reverse()
    _parent = None

    x = None
    for _cate in _list:
        _find = list(filter(lambda c: c['name'] == _cate))  # c is category
        
        filter()

    return _parent
