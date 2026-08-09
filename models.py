from pydantic import BaseModel

class Incident(BaseModel):
    date: str
    incident_time: str
    incident_description: str
    sap_number: str
    location: str
    response_time: str
    downtime_duration: str


class IncidentUpdate(BaseModel):
    incident_description: str
    downtime_duration: str