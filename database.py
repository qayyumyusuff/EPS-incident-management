import sqlite3


def get_connection(database_name="incidents.db"):
    connection = sqlite3.connect(database_name)
    connection.row_factory = sqlite3.Row
    return connection

def initialize_database(database_name = "incidents.db"):
    connection = get_connection(database_name)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        incident_time TEXT NOT NULL,
        incident_description TEXT NOT NULL,
        sap_number TEXT NOT NULL UNIQUE,
        location TEXT NOT NULL,
        response_time TEXT NOT NULL,
        downtime_duration TEXT NOT NULL
        )
    """)

    connection.commit() 
    connection.close()



initialize_database()