from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from authentication.models import CustomUser

class NotificationsTests(APITestCase):
    def setUp(self):
        # Create tests users
        self.user1 = CustomUser.objects.create_user(email='user1@test.com', password='test123')
        self.user2 = CustomUser.objects.create_user(email='user2@test.com', password='test123')
        # Log the user 1 in
        response1 = self.client.post(reverse('login'), {'email': 'user1@test.com', 'password': 'test123'})
        # Get the access token from the response
        response1_content = response1.json()
        self.token1 = response1_content.get('access_token')
        # Log user 2 in
        response2 = self.client.post(reverse('login'), {'email': 'user2@test.com', 'password': 'test123'})
        # Get the access token from the response
        response2_content = response2.json()
        self.token2 = response2_content.get('access_token')

    def test_send_notification(self):
        # Send notification to user 2
        response = self.client.post(reverse('notification-send'), {'recipient_id': self.user2.id, 'content': 'You have a new invitation'}, headers={'Authorization':f'Bearer {self.token1}'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def get_notifications(self):
        # Send notification to user 2
        self.client.post(reverse('notification-send'), {'recipient_id': self.user2.id, 'content': 'You have a new invitation'}, headers={'Authorization': f'Bearer {self.token1}'}, format='json')

        # Retrieve notifications for user 2
        response = self.client.get(reverse('notifications-get'), headers={'Authorization': f'Bearer {self.token2}'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)