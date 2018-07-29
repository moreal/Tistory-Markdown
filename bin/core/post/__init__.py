from pytistory import PyTistory


class Post():
    def __init__(self, pytistory: PyTistory):
        self.pytistory = pytistory

    def upload(self, filename):
        """마크다운 파일을 파싱, Tistory에 업로드 하는 함수입니다

        :filename 업로드할 파일들입니다!

        """
        pytistory = self.pytistory
        pytistory.post.write()

    def create(self, filename=None, title="Title", category=[]):
        """샘플 md 다운 파일을 만드는 함수 입니다

        :filename 파일 이름입니다
        :title 글의 제목입니다
        :description

        """

        if filename is None:
            filename = title + ".md"

        