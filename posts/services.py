from posts.models import Post
from tags.models import Tag


def add_tags_to_post(post_id, tags):
    post = Post.objects.get(pk=post_id)

    for tag_id in filter(lambda n: n != ',', tags):
        tag = Tag.objects.get(pk=tag_id)
        tag.posts.add(post)
