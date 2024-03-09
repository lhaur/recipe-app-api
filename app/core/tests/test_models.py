"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a auser with an email is successful."""
        email = "test@lassi.dev"
        password = "passwordtest123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test is email normalized for new users."""
        sample_emails = [
            ['test1@lassi.DEV', 'test1@lassi.dev'],
            ['Test2@Lassi.dev', 'Test2@lassi.dev'],
            ['TEST3@LASSI.DEV', 'TEST3@lassi.dev'],
            ['test4@LASSI.dev', 'test4@lassi.dev']
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'testpass')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'testpass')

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            'admin@lassi.dev',
            'testpass'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
