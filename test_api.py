import pytest

from fastapi.testclient import TestClient


import api
from database import get_connection, initialize_database


TEST_DB = "test_incidents.db"


def get_test_connection():
    return get_connection(TEST_DB)


@pytest.fixture(autouse=True)
def reset_test_database():
    initialize_database(TEST_DB)

    connection = get_connection(TEST_DB)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM incidents")

    connection.commit()
    connection.close()

api.get_connection = get_test_connection


client = TestClient(api.app)


def test_get_incidents():
    response = client.get("/incidents")
    assert response.status_code == 200


def test_create_incident():
    incident_data = {
        "date": "09/08/2026",
        "incident_time": "21:00",
        "incident_description": "Automated Test incident",
        "sap_number": "Test-001",
        "location": "Test Substation",
        "response_time": "5 minutes",
        "downtime_duration": "10 minutes"
    }
    response = client.post(
        "/incidents",
        json=incident_data
    )

    assert response.status_code == 201


def test_update_incident():
    new_incident = {
        "date": "09/08/2026",
        "incident_time": "21:30",
        "incident_description": "Original description",
        "sap_number": "TEST-UPDATE-001",
        "location": "Test Substation",
        "response_time": "5 minutes",
        "downtime_duration": "10 minutes"
    }

    client.post(
        "/incidents",
        json=new_incident
    )

    updated_data = {
        "incident_description": "Updated description",
        "downtime_duration": "20 minutes"
    }

    response = client.put(
        "/incidents/TEST-UPDATE-001",
        json=updated_data
    )

    assert response.status_code == 200


    get_response = client.get("/incidents")
    incidents = get_response.json()

    updated_incident = next(
        incident
        for incident in incidents
        if incident["sap_number"] == "TEST-UPDATE-001"
    )

    assert updated_incident["incident_description"] == "Updated description"
    assert updated_incident["downtime_duration"] == "20 minutes"


def test_delete_incident():
    new_incident = {
        "date": "09/08/2026",
        "incident_time": "21:45",
        "incident_description": "Incident to delete",
        "sap_number": "TEST-DELETE-001",
        "location": "Test Substation",
        "response_time": "5 minutes",
        "downtime_duration": "10 minutes"
    }

    client.post(
        "/incidents",
        json=new_incident
    )

    response = client.delete(
        "/incidents/TEST-DELETE-001"
    )

    assert response.status_code == 200

    get_response = client.get("/incidents")
    incidents = get_response.json()

    deleted_incident = next(
        (
            incident
            for incident in incidents
            if incident["sap_number"] == "TEST-DELETE-001"
        ),
        None
    )

    assert deleted_incident is None


def test_update_incident_not_found():
    updated_data = {
        "incident_description": "Does not matter",
        "downtime_duration": "5 minutes"
    }

    response = client.put(
        "/incidents/DOES-NOT-EXIST",
        json=updated_data
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "SAP number not found"


def test_duplicate_incident():
    new_incident = {
        "date": "09/08/2026",
        "incident_time": "22:00",
        "incident_description": "Duplicate test",
        "sap_number": "TEST-DUPLICATE-001",
        "location": "Test Substation",
        "response_time": "5 minutes",
        "downtime_duration": "10 minutes"
    }

    client.post(
        "/incidents",
        json=new_incident
    )

    response = client.post(
        "/incidents",
        json=new_incident
    )

    assert response.status_code == 409
    assert response.json()["detail"] == "SAP number already exists"


def test_delete_incident_not_found():
    response = client.delete(
        "/incidents/DOES-NOT-EXIST"
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "SAP number not found"