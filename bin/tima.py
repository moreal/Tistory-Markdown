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

    if cmd == "post":
        try:
            cmd = args[0]
            if cmd == "create":
                create(args[1])
            elif cmd == "upload":
                upload(args[1])
            elif cmd == "list":
                show_list()
        except IndexError as e:
            click.echo('too less args..')

    click.echo("Test!!")


if __name__ == "__main__":
    tima()
