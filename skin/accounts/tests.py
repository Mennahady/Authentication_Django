from django.test import TestCase
from django.core import mail
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_password_reset_email(self):
        """Test that password reset email is sent"""
        response = self.client.post(reverse('password_reset_request'), {
            'email': 'test@example.com'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Password Reset Request')
