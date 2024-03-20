import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Partner
from ..serializers import PartnerSerializer


class PartnerViewSetTests(APITestCase):
    fixtures = ["partners.json"]

    def test_list_partners(self):
        """
        Ensure we can list all partners
        """

        url = reverse("partner-list")
        response = self.client.get(url)
        partners = Partner.objects.all()
        serializer = PartnerSerializer(partners, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_partner(self):
        """
        Ensure we can retrieve a single partner by ID.
        """

        partner = Partner.objects.first()
        url = reverse("partner-detail", args=[partner.pk])
        response = self.client.get(url)
        serializer = PartnerSerializer(partner)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
