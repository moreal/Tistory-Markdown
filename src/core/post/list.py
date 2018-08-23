from core import Tima
from typing import List

import click


def _list(tima: Tima) -> List:
    posts = tima.pytistory.post.list(
        blog_name=tima.blog_name
    )['item']['posts']

    for index, post in enumerate(posts):
        click.echo(f"[+] {index} : {post['title']} / {post['postUrl']}")
