import sqlite3

from fastapi import FastAPI, HTTPException
from database import get_connection
from models import Incident, IncidentUpdate


app = FastAPI(
    title="EPS Incident Management API",
    description="REST API for managing electrical incident records.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "EPS Incident Management API"
    }


@app.post("/incidents", status_code=201)
def create_incident(incident: Incident):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO incidents (
                date,
                incident_time,
                incident_description,
                sap_number,
                location,
                response_time,
                downtime_duration
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                incident.date,
                incident.incident_time,
                incident.incident_description,
                incident.sap_number,
                incident.location,
                incident.response_time,
                incident.downtime_duration
            )
        )

        connection.commit()

    except sqlite3.IntegrityError:
        connection.close()

        raise HTTPException(
            status_code=409,
            detail="SAP number already exists"
        )

    connection.close()

    return {
        "message": "Incident created successfully"
    }


@app.get("/incidents")
def get_incidents():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM incidents")
    incidents = cursor.fetchall()

    connection.close()

    return [dict(incident) for incident in incidents]


@app.put("/incidents/{sap_number}")
def update_incident(
    sap_number: str,
    updated_data: IncidentUpdate
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE incidents
        SET incident_description = ?,
            downtime_duration = ?
        WHERE sap_number = ?
        """,
        (
            updated_data.incident_description,
            updated_data.downtime_duration,
            sap_number
        )
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()

        raise HTTPException(
            status_code=404,
            detail="SAP number not found"
        )

    connection.close()

    return {
        "message": "Incident updated successfully"
    }

@app.delete("/incidents/{sap_number}")
def delete_incident(sap_number: str):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM incidents WHERE sap_number = ?",
        (sap_number,)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()

        raise HTTPException(
            status_code=404,
            detail="SAP number not found"
        )

    connection.close()

    return {
        "message": "Incident deleted successfully"
    }