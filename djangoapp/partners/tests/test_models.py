import json
from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import Partner
from ..serializers import PartnerSerializer


class PartnerModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        with open("partners/fixtures/fixture_pdvs.json") as f:
            fixture_data = json.load(f)

        for data in fixture_data:
            serializer = PartnerSerializer(data=data["fields"])
            if serializer.is_valid():
                serializer.save()
            else:
                raise ValueError(f"Invalid data: {serializer.errors}")

    def test_partner_creation(self):
        """
        Ensure we can create a new Partner instance.
        """

        # Act: Create a new Partner instance
        new_partner = {
            "id": "teste",
            "tradingName": "New Partner",
            "ownerName": "Renato Cariri",
            "document": "12345678912345/0001",
            "coverageArea": {
                "type": "MultiPolygon",
                "coordinates": [
                    [[[30, 20], [45, 40], [10, 40], [30, 20]]],
                    [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]],
                ],
            },
            "address": {"type": "Point", "coordinates": [-52.57421, -21.785741]},
        }

        # Convert data to JSON serializable format
        new_partner_json = json.dumps(new_partner)

        # Pass data through the serializer
        serializer = PartnerSerializer(data=new_partner)

        if serializer.is_valid():
            new_partner = serializer.save()
        else:
            raise ValueError(f"Invalid data: {serializer.errors}")

        # Assert: Ensure the new instance is of Partner type
        self.assertIsInstance(new_partner, Partner)

    def test_document_field_unique(self):
        """
        Ensure that the document field is unique.
        """
        existing_partner = Partner.objects.first()

        new_partner = Partner(
            tradingName="New Partner",
            ownerName="Renato Cariri",
            document=existing_partner.document,
            coverageArea=existing_partner.coverageArea,
            address=existing_partner.address,
        )
        with self.assertRaises(ValidationError):
            new_partner.full_clean()
