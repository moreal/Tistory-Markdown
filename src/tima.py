#!/usr/bin/python3
import click

from core import Tima

"""Command Map
- post
    - create (with template)
    - upload (by env conf)
    - list (list)
- info
    - version
"""


@click.command()
@click.argument('cmd')
@click.argument('args', nargs=-1)
def tima(cmd, args):
    tima = Tima()

    from core.router import Router

    Router.command_route(tima, cmd, args)


if __name__ == "__main__":
    tima()
