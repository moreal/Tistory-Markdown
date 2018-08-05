"""Need front matter
:title: AnyStr
게시물의 제목입니다

:visibility: int
0: 비공개 1: 보호 2: 공개 3: 발행

:tags: list[AnyStr...]
태그들을 list로 받아야 합니다

:category: list[AnyStr...] or int
category 계층 list를 받거나 int 값을 직접 받아서 post합니다. 기본값은 0입니다
"""


def create(filename):
    with open(filename, 'w') as f:
        from config import DEFAULT_MARKDOWN
        f.write(DEFAULT_MARKDOWN)
