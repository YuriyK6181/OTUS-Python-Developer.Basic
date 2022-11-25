from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from veloride.models import Bike


class BikesListTestCase(TestCase):
    fixtures = [
        "bike_classes.fixture.json",
        "bike_types.fixture.json",
        "bike_manufacturers.fixture.json",
        "bikes.fixture.json",
    ]

    def test_veloride(self):

        url = reverse("veloride:index")
        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)

        bikes = (
            Bike
            .objects
            .select_related("bike_class")
            .select_related("bike_type")
            .select_related("manufacturer")
            .filter(archived=False)
            .order_by("pk")
            .all()
        )
        print("List of Bikes:", bikes)
        bikes_in_context = response.context["veloride"]
        print("List in context:", bikes_in_context)
        print("Compare as str() test result:", str(bikes) == str(bikes_in_context))
        self.assertEqual(len(bikes), len(bikes_in_context))
        for a1, a2 in zip(bikes, bikes_in_context):
            self.assertEqual(a1.pk, a2.pk)

