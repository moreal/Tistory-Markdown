from core import Tima
from typing import List, AnyStr, Type, Dict

import click


def is_type_list(_type: Type, _list: List[AnyStr]) -> bool:
    for el in _list:
        if type(el) != _type:
            return False
    return True


def get_category(_tima: Tima, _category: List[AnyStr]) -> int:
    resp = _tima.pytistory.category.list(blog_name=_tima.blog_name)
    categories = resp['item']['categories']
    
    if isinstance(_category, str):
        _category = _category.strip()
    elif isinstance(_category, list):
        _category = "/".join(_category)

    categories = list(filter(lambda x: x['label'] == _category, categories))
    category = categories[0]['id'] if len(categories) > 0 else None

    if category is None:
        click.echo(f"[!] Wrong Category :: Input is {_category}")
        exit(0)
    else:
        return category
