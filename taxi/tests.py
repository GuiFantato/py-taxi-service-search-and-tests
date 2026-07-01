from django.test import TestCase
from django.urls import reverse

from taxi.models import Driver


class DriverSearchTests(TestCase):
    def setUp(self):
        self.driver1 = Driver.objects.create_user(
            username="john",
            password="test12345",
            license_number="ABC12345",
        )

        self.driver2 = Driver.objects.create_user(
            username="michael",
            password="test12345",
            license_number="XYZ12345",
        )

        self.client.login(
            username="john",
            password="test12345",
        )

    def test_search_driver_by_username(self):
        response = self.client.get(
            reverse("taxi:driver-list"),
            {"search": "john"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "john")
        self.assertNotContains(response, "michael")

    def test_search_with_empty_query_returns_all_drivers(self):
        response = self.client.get(
            reverse("taxi:driver-list"),
            {"search": ""},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "john")
        self.assertContains(response, "michael")
