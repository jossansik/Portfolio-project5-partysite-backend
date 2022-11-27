from django.test import TestCase
from posts.services import add_tags_to_post
from profiles.models import Profile
from django.contrib.auth.models import User
from posts.models import Post
from tags.models import Tag
from categories.models import Category


class AddTagsToPostTest(TestCase):
    """
    When running this test, tags should be added to the post.
    This is achived by connecting tag to a post.
    The purpose of this is that the posts can be filtered by tags.
    The reason why tags are splitted by ',' within the add_tags_to_post 
    function is that it is submitted as a comma separated list.
    The test proves that the tag gets connected to the post.
    """


    def test_can_add_tag_to_post(self):
        """
        When there are one tag submitted to a post,
        It should be connected,
        Then we should find the post by tag submitted.
        """

        # Arrange
        user = User.objects.create_user(
            'jossan.svensson', 'blah@blah.com', 'testpassword')
        category = Category.objects.create(name = 'Halloween')
        tag1 = Tag.objects.create(name = 'tag1', category = category)
        post = Post.objects.create(
            title = 'Flexidrop', owner = user, category = category)
        tag_string = str(tag1.id)

        # Act
        add_tags_to_post(post.id, tag_string)

        # Assert
        new_post_with_tags = Post.objects.filter(post_tags = tag1.id)
        self.assertEqual(new_post_with_tags[0], post)


    def test_when_no_tags_submitted_expect_no_tags_on_post(self):
        """
        When there are no tag submitted to a post,
        It should not be connected to any tags,
        Then we should not find any post for the tag.
        """

        # Arrange
        user = User.objects.create_user(
            'jossan.svensson1', 'blah1@blah.com', 'testpassword')
        category = Category.objects.create(name = 'Halloween')
        tag1 = Tag.objects.create(name = 'tag1', category = category)
        post = Post.objects.create(
            title = 'Flexidrop1', owner = user, category = category)
        tag_string = ""

        # Act
        add_tags_to_post(post.id, tag_string)

        # Assert
        new_post_with_tags = Post.objects.filter(post_tags = tag1.id)
        self.assertEqual(new_post_with_tags.count(), 0)


    def test_when_two_tags_submitted_expect_match_on_both_tags(self):
        """
        When there are two tags submitted to a post,
        It should be connected to both tags,
        Then we should be able to find post by both tags.
        """

        # Arrange
        user = User.objects.create_user(
            'jossan.svensson2', 'blah2@blah.com', 'testpassword')
        category = Category.objects.create(name = 'Halloween')
        tag1 = Tag.objects.create(name = 'tag5', category = category)
        tag2 = Tag.objects.create(name = 'tag6', category = category)
        post = Post.objects.create(
            title = 'Flexidrop2', owner = user, category = category)
        tag_string = str(tag1.id) + ',' + str(tag2.id)

        # Act
        add_tags_to_post(post.id, tag_string)

        # Assert
        new_post_with_tags1 = Post.objects.filter(post_tags = tag1.id)
        self.assertEqual(new_post_with_tags1[0], post)
        new_post_with_tags2 = Post.objects.filter(post_tags = tag2.id)
        self.assertEqual(new_post_with_tags2[0], post)

