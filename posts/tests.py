from django.test import TestCase
from posts.services import add_tags_to_post
from profiles.models import Profile
from django.contrib.auth.models import User
from posts.models import Post
from tags.models import Tag
from categories.models import Category


class AddTagsToPostTest(TestCase):
    def test_can_add_tags_to_post(self):
        # Arrange
        user = User.objects.create_user('jossan.svensson', 'blah@blah.com', 'testpassword')
        category = Category.objects.create(name='Halloween')
        tag1 = Tag.objects.create(name='tag1', category=category)
        tag2 = Tag.objects.create(name='tag2', category=category)
        post = Post.objects.create(title='Flexidrop', owner=user, category=category)
        tag_string = str(tag1.id) + ',' + str(tag2.id)

        # Act
        add_tags_to_post(post.id, tag_string)

        # Assert
        new_post_with_tags = Post.objects.filter(post_tags=tag1.id)
        self.assertEqual(new_post_with_tags[0], post)
