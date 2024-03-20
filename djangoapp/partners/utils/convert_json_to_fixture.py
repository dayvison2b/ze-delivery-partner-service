import json
import argparse


def convert_json_to_fixture_format(json_file):
    """
    Converts a JSON file containing partner data into a list of dictionaries in the Django fixture format.

    The JSON file should have a top-level key 'pdvs' containing a list of partner dictionaries. Each partner
    dictionary should have the following keys:
    - 'id': unique identifier for the partner
    - 'tradingName': the trading name of the partner
    - 'ownerName': the name of the partner's owner
    - 'document': the document number of the partner
    - 'coverageArea': a GeoJSON geometry representing the partner's coverage area
    - 'address': a GeoJSON point representing the partner's address

    The resulting fixture data is written to 'partners/fixtures/fixture_pdvs.json'.

    Args:
        json_file (str): Path to the JSON file containing the partner data.

    Returns:
        list: A list of dictionaries representing the partner data in the Django fixture format.

    Raises:
        FileNotFoundError: If the specified JSON file is not found.
        json.JSONDecodeError: If the JSON data cannot be decoded.
    """
    try:
        with open(json_file) as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file '{json_file}' not found.")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Error decoding JSON data in '{json_file}': {e}")

    fixtures = []
    for partner in data["pdvs"]:
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

    with open("partners/fixtures/fixture_pdvs.json", "w") as f:
        json.dump(fixtures, f, indent=4)

    return fixtures


def main():
    """
    Main function to parse command-line arguments and call the conversion function.
    """
    parser = argparse.ArgumentParser(
        description="Convert JSON data to Django fixture format."
    )
    parser.add_argument("json_file", help="Path to the JSON file containing the data")
    args = parser.parse_args()
    convert_json_to_fixture_format(args.json_file)


if __name__ == "__main__":
    main()
