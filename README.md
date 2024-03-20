# Django GeoJSON Partner Service

This project is a Django application developed for the Ze-delivery backend challenge. It provides a service that manages partners, allowing the creation, retrieval by ID, and searching for the nearest partner based on a given location. The service is built using Django, Docker, and PostgreSQL, making it easy to deploy and ensuring consistency across different environments.

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
git clone https://github.com/your-repo/django-geojson-partner-service.git
```

2. Navigate to the project directory.

```bash
cd django-geojson-partner-service
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

## Additional Notes

- The GeoJSON format was chosen to represent partner coverage areas and addresses due to its compatibility with geospatial data.
- Implementing the search functionality based on GeoJSON coverage areas can be challenging due to the complexity of geospatial calculations.
- The service is designed to be self-contained and scalable, making it suitable for handling large volumes of partner data and search queries.

By following the instructions provided in this README.md file, you should be able to execute and deploy the service successfully. If you encounter any issues or require further assistance, please don't hesitate to reach out.