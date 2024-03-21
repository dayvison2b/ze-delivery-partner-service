# Django GeoJSON Partner Service

This project is a Django application developed for the [Ze-delivery backend challenge](https://github.com/ab-inbev-ze-company/ze-code-challenges/blob/master/backend.md#backend-challenge). It provides a service that manages partners, allowing the creation, retrieval by ID, and searching for the nearest partner based on a given location. The service is built using Django, Docker, and PostgreSQL, making it easy to deploy and ensuring consistency across different environments.

## Features

- **Create Partner**: Save partner information in the database, including trading name, owner name, document, coverage area, and address. The coverage area and address follow the GeoJSON format.

- **Load Partner by ID**: Retrieve a specific partner by its unique ID, including all associated fields.

- **Search Partner**: Given a specific location (longitude and latitude coordinates), find the nearest partner whose coverage area includes the location.

## Technical Details

- **Programming Language**: Python
- **Framework**: Django, rest-framework
- **Database**: PostgreSQL
- **Geospatial Data Format**: GeoJSON
- **Containerization**: Docker
- **Cross-platform Compatibility**: Designed to run on different operating systems.

## Prerequisites

Before running the project, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

To execute this service locally, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/dayvison2b/ze-delivery-partner-service.git
```

2. Navigate to the project directory.

```bash
cd ze-delivery-partner-service
```

3. Create a `.env` file in the `dotenv_files/` directory following the .env-example in the directory:

4. Build the Docker images:

```bash
docker-compose build
```

5. Start the Docker containers:

```bash
docker-compose up
```

The Django application will be accessible at http://localhost:8000.

# Testing

The application is able to pass all the requirements:

### 1.1. Create a Partner

You can create a new partner by sending a POST request to the `/partners/` endpoint with the following data format:

```json
{
  "id": 1,
  "tradingName": "Adega da Cerveja - Pinheiros",
  "ownerName": "Zé da Silva",
  "document": "1432132123891/0001",
  "coverageArea": {
    "type": "MultiPolygon",
    "coordinates": [
      [[[30, 20], [45, 40], [10, 40], [30, 20]]],
      [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]]
    ]
  },
  "address": {
    "type": "Point",
    "coordinates": [-46.57421, -21.785741]
  }
}
```

#### Loading Partners from a JSON File

You can use the provided [pdvs.json](https://github.com/ab-inbev-ze-company/ze-code-challenges/blob/master/files/pdvs.json) file, which contains hundreds of partner information, to load them all into the database using the following customized command:

```
python manage.py loaddata pdvs.json --serializer PartnerSerializer
```

The pdvs.json file is located in the `djangoapp/partners/fixtures` directory, and the command will automatically recognize it without needing to specify the path.

Below, you can see an example of how these partners might be represented on a map:
![map](https://github.com/ab-inbev-ze-company/ze-code-challenges/blob/master/files/images/pdvs.png)

### 1.2. [Load partner by id](https://github.com/ab-inbev-ze-company/ze-code-challenges/blob/master/backend.md#12-load-partner-by-id):

To retrieve a specific partner by its ID, you can send a GET request to the `/partners/{id}/` endpoint, where {id} is the ID of the partner you want to retrieve.

For example, to retrieve the partner with ID 1, you can send a GET request to `localhost:8000/partners/1/`

### 1.3. [Search partner](https://github.com/ab-inbev-ze-company/ze-code-challenges/blob/master/backend.md#13-search-partner):

To search for the nearest partner that covers a specific location, you can send a GET request to the `/search/` endpoint with the `lat` and `long` query parameters representing the location's latitude and longitude, respectively.

For example, to search for the nearest partner covering the location with latitude `-21.785741` and longitude `-46.57421`, you can send a GET request to
`localhost:8000/search/?lat=-21.785741&long=-46.57421`

If a partner is found, the API will return the partner's information. Otherwise, it will return a 404 status code with the message "No partner found for the given location."

## Additional Notes

- The GeoJSON format was chosen to represent partner coverage areas and addresses due to its compatibility with geospatial data.
- Implementing the search functionality based on GeoJSON coverage areas can be challenging due to the complexity of geospatial calculations.
- The service is designed to be self-contained and scalable, making it suitable for handling large volumes of partner data and search queries.

By following the instructions provided in this README.md file, you should be able to execute and deploy the service successfully. If you encounter any issues or require further assistance, please don't hesitate to reach out.