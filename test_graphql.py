#!/usr/bin/env python3
"""
Simple test script for the GraphQL API with spatial queries
"""
import requests
import json

# Test GraphQL endpoint
url = "http://localhost:8000/graphql/"

# Test query to get all locations
query = """
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
"""

# Test spatial query to get nearby locations
nearby_query = """
query {
  nearbyLocations(lat: 40.7128, lng: -74.0060, radiusKm: 5.0) {
    id
    name
    latitude
    longitude
    distance
  }
}
"""

# Test mutation to create a location
mutation = """
mutation {
  createLocation(
    name: "Test Location"
    description: "A test location"
    latitude: 40.7128
    longitude: -74.0060
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
"""


def test_graphql():
    print("Testing GraphQL API with spatial queries...")
    
    # Test the basic query
    try:
        response = requests.post(url, json={'query': query})
        print(f"Query response status: {response.status_code}")
        print(f"Query response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error testing query: {e}")
    
    # Test the spatial query
    try:
        response = requests.post(url, json={'query': nearby_query})
        print(f"Nearby query response status: {response.status_code}")
        print(f"Nearby query response: "
              f"{json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error testing nearby query: {e}")
    
    # Test the mutation
    try:
        response = requests.post(url, json={'query': mutation})
        print(f"Mutation response status: {response.status_code}")
        print(f"Mutation response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error testing mutation: {e}")


if __name__ == "__main__":
    test_graphql() 