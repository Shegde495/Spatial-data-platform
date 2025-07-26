# Simple Spatial Data GraphQL API

A simple Django project with GraphQL API for managing location data.

## Features

- Simple Location model with name, description, and coordinates
- GraphQL API with CRUD operations
- Interactive GraphiQL interface
- Django admin interface

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

4. Run the server:
```bash
python manage.py runserver
```

## Usage

- **GraphQL Interface**: Visit `http://localhost:8000/graphql/` for the interactive GraphiQL interface
- **Admin Interface**: Visit `http://localhost:8000/admin/` to manage data through Django admin

## GraphQL Queries

### Get all locations
```graphql
query {
  allLocations {
    id
    name
    description
    latitude
    longitude
    createdAt
  }
}
```

### Get a specific location
```graphql
query {
  location(id: 1) {
    id
    name
    description
    latitude
    longitude
  }
}
```

## GraphQL Mutations

### Create a location
```graphql
mutation {
  createLocation(
    name: "Central Park"
    description: "A beautiful park in NYC"
    latitude: 40.7829
    longitude: -73.9654
  ) {
    location {
      id
      name
      latitude
      longitude
    }
    success
    errors
  }
}
```

### Update a location
```graphql
mutation {
  updateLocation(
    id: 1
    name: "Updated Park Name"
    description: "Updated description"
  ) {
    location {
      id
      name
      description
    }
    success
    errors
  }
}
```

### Delete a location
```graphql
mutation {
  deleteLocation(id: 1) {
    success
    errors
  }
}
``` 