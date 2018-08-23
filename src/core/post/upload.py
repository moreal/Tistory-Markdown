from core import Tima
import frontmatter
from typing import AnyStr

import mistune
from ext.highlight import HighlightRenderer


def _upload(tima: Tima, filename: AnyStr) -> None:
    with open(filename, 'r') as f:
        post = frontmatter.loads(f.read())
        content, metadata = post.content, post.metadata

        title = metadata['title'] or "Title"
        visibility = metadata['visibility'] or 2
        tags = metadata['tags'] or []
        categories = metadata['category'] or []

        from core.util import get_category
        category_num = get_category(tima, categories)

        renderer = HighlightRenderer()
        markdown = mistune.Markdown(renderer=renderer)

        tima.pytistory.post.write(
            title,
            blog_name=tima.blog_name,
            visibility=visibility,
            category=category_num,
            content=markdown(content),
            tag=tags
        )
