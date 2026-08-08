# EPS Incident Management System

A backend API for recording and managing electrical power system incidents.

I started this project as a simple Python console application and later developed it into a REST API using FastAPI. The project is based on incident-management workflows I am familiar with from electrical engineering operations, while allowing me to build practical software development skills.

## Features

- Create a new incident
- View recorded incidents
- Update incident description and downtime duration
- Delete incidents
- Prevent duplicate SAP numbers
- Store incident data persistently using SQLite
- Return appropriate HTTP status codes for API requests
- Interactive API testing through Swagger UI

## Tech Stack

- Python
- FastAPI
- Pydantic
- SQLite
- Git and GitHub

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| POST | `/incidents` | Create a new incident |
| GET | `/incidents` | View all incidents |
| PUT | `/incidents/{sap_number}` | Update an incident |
| DELETE | `/incidents/{sap_number}` | Delete an incident |

## Running the Project

Clone the repository and move into the project directory:

```bash
git clone https://github.com/qayyumyusuff/EPS-incident-management.git
cd EPS-incident-management
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create the SQLite database:

```bash
python database.py
```

Start the FastAPI development server:

```bash
python -m fastapi dev api.py
```

Then open the Swagger documentation at:

`http://127.0.0.1:8000/docs`

## Project Structure

```text
EPS-incident-management/
├── api.py              # FastAPI application and API endpoints
├── database.py         # SQLite database setup
├── main.py             # Original console prototype
├── requirements.txt    # Python dependencies
├── README.md
└── .gitignore
```

```markdown
## Project Status

The project currently includes a working REST API with SQLite persistence.

Planned improvements:
- Authentication and user roles
- Automated testing
- Improved project structure
- Cloud deployment