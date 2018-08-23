from core import Tima
import frontmatter
from typing import AnyStr


def _upload(tima: Tima, filename: AnyStr) -> None:
    with open(filename, 'r') as f:
        post = frontmatter.loads(f.read())
        content, metadata = post.content, post.metadata
        
        title = metadata['title'] or "Title"
        visibility = metadata['visibility'] or 2
        tags = metadata['tags'] or []
        categories = metadata['category'] or []
        
        from core.post.util import get_category
        category_num = get_category(categories)

        tima.pytistory.post.write(
            title,
            blog_name=tima.blog_name,
            visibility=visibility,
            category=category_num,
            content=content,
            tag=tags
        )
