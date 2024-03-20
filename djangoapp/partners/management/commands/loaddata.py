import json
from django.core.management.commands.loaddata import Command as LoadDataCommand
from django.core.exceptions import ImproperlyConfigured
from partners import serializers as partner_serializers


def convert_json_to_fixture_format(json_data):
    """
    Convert JSON data to a list of dictionaries in the Django fixture format.

    Args:
        json_data (dict): JSON data containing a list of partner data under the 'pdvs' key.

    Returns:
        list: A list of dictionaries representing the partner data in the Django fixture format.
    """
    fixtures = []
    for partner in json_data.get("pdvs", []):
        fixture = {
            "model": "partners.Partner",
            "fields": {
                "id": partner["id"],
                "tradingName": partner["tradingName"],
                "ownerName": partner["ownerName"],
                "document": partner["document"],
                "coverageArea": partner["coverageArea"],
                "address": partner["address"],
            },
        }
        fixtures.append(fixture)
    return fixtures


class Command(LoadDataCommand):
    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            "--serializer",
            type=str,
            help="Serializer class to use for deserialization",
        )

    def handle(self, *fixture_labels, **options):
        serializer_name = options.get("serializer")

        if serializer_name:
            for fixture_label in fixture_labels:
                try:
                    with open(f"partners/fixtures/{fixture_label}") as f:
                        json_data = json.load(f)
                    fixtures = convert_json_to_fixture_format(json_data)
                    self.load_from_fixtures(fixtures, serializer_name)
                except FileNotFoundError:
                    self.stderr.write(
                        self.style.ERROR(f"File not found: {fixture_label}")
                    )
                except json.JSONDecodeError:
                    self.stderr.write(
                        self.style.ERROR(f"Invalid JSON format in {fixture_label}")
                    )
        else:
            super().handle(*fixture_labels, **options)

    def load_from_fixtures(self, fixtures, serializer_name):
        """
        Load fixtures using the specified serializer.

        Args:
            fixtures (list): A list of dictionaries representing the partner data in the Django fixture format.
            serializer_name (str): The name of the serializer class to use for deserialization.
        """
        serializer_class = getattr(partner_serializers, serializer_name, None)
        if serializer_class is None:
            raise ImproperlyConfigured(
                f"Serializer '{serializer_name}' not found in partners.serializers"
            )

        for fixture in fixtures:
            serializer = serializer_class(data=fixture["fields"])
            if serializer.is_valid():
                serializer.save()
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Data saved successfully using {serializer_class.__name__}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.ERROR(f"Validation error: {serializer.errors}")
                )
