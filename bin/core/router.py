import click
from core import Tima
from typing import AnyStr, List


class Router():
    # @staticmethod7
    def command_route(tima: Tima, cmd: AnyStr, args: List[AnyStr]) -> None:
        """cmd와 args를 기반으로 라우팅 해주는 메소드입니다

        tima: 블로그 관련 업무를 처리할 Tima class 인스턴스입니다\n

        cmd: 명령어 입니다\n

        args: 명령의 인자로 주어진 값들입니다\n
        """

        from core.info import Info

        try:
            if cmd == "info":
                if args[0] == "version":
                    click.echo(tima.info.version())
            elif cmd == "post":
                if args[0] == "create":
                    tima.post.create(args[1])
                elif args[0] == "list":
                    tima.post.list()
                elif args[0] "upload":
                    tima.post.upload()
        except IndexError as e:
            click.echo("[!] Tima :: input args are too short..")