import sqlite3

connection = sqlite3.connect("incidents.db")
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
