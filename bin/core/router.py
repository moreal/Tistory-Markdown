from core import Tima
from typing import AnyStr, List


class Router():
    @staticmethod
    def command_route(tima: Tima, cmd: AnyStr, args: List[AnyStr]) -> None:
        """cmd와 args를 기반으로 라우팅 해주는 메소드입니다
        tima: Tima
        블로그 관련 업무를 처리할 Tima class 인스턴스입니다

        cmd: AnyStr
        명령어 입니다

        args: List[AnyStr]
        명령의 인자로 주어진 값들입니다
        """

        if cmd == "info":
            tima.info()
