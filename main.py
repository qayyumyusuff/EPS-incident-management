incidents = []

def display_menu():
    print("=" * 40)
    print("EPS INCIDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Create Incident")
    print("2. View Incidents")
    print("3. Update Incident")
    print("4. Delete Incident")
    print("5. Exit")

def create_incident():

    
    print("\nCreate New Incident")
    print("-" * 40)


    date = input("Date: ")
    incident_time = input("Incident time: ")
    incident_description = input("Incident description: ")
    sap_number = input("SAP number: ")
    location = input("Location: ")
    response_time = input("Response time: ")
    downtime_duration = input("Downtime Duration: ")


    print("\nIncident Summary")
    print("-" * 40)
    print(f"Date: {date}")
    print(f"Incident Time: {incident_time}")
    print(f"Incident Description: {incident_description}")
    print(f"SAP Number: {sap_number}")
    print(f"Location: {location}")
    print(f"Response Time: {response_time}")
    print(f"Downtime Duration: {downtime_duration}")


    incident ={
            "date": date,
            "incident_time": incident_time,
            "incident_description": incident_description,
            "sap_number": sap_number,
            "location": location,
            "response_time": response_time,
            "downtime_duration": downtime_duration,
        }
    
    
    incidents.append(incident)

def view_incident():
    print("\nView Incidents")
    print("-" * 40)

    if len(incidents) == 0:
        print("No incidents found.")
        return

    for incident in incidents:
        print(f"Date: {incident['date']}")
        print(f"Incident Time: {incident['incident_time']}")
        print(f"Incident Description: {incident['incident_description']}")
        print(f"SAP Number: {incident['sap_number']}")
        print(f"Location: {incident['location']}")
        print(f"Response Time: {incident['response_time']}")
        print(f"Downtime Duration: {incident['downtime_duration']}")
        print("-" * 40)

            
def update_incident():
    print("\nUpdate Incident")
    print("-" * 40)

    sap_number = input("Enter SAP Number: ")
    print(f"Searching for SAP Number: {sap_number}")

    for incident in incidents:
        if incident["sap_number"] == sap_number:
            print("\nIncident found!")
            print(f"SAP Number: {incident['sap_number']}")
            print(
                f"Current Description: "
                f"{incident['incident_description']}"
            )
            print(
                f"Current Downtime Duration: "
                f"{incident['downtime_duration']}"
            )

            new_description = input("New Description: ")
            new_downtime_duration = input("New Downtime Duration: ")

            incident["incident_description"] = new_description
            incident["downtime_duration"] = new_downtime_duration

            print("\nIncident updated successfully.")
            return

    print("SAP number not found. Please try again.")

def delete_incident():
    print("\nDelete Incident")
    print("-" * 40)

    sap_number = input("Enter SAP Number: ")

    for incident in incidents:
        if incident["sap_number"] == sap_number:
            incidents.remove(incident)
            print("\nIncident deleted successfully.")
            return

    print("SAP number not found. Please try again.")

def main():
    while True:
        display_menu()
        choice = input("Select an option: ")


        if choice == "1":
            create_incident()

        elif choice == "2":
            view_incident()
            
        elif choice == "3":
            update_incident()
            
        elif choice == "4":
            delete_incident()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")     

        print() 


if __name__ == "__main__":
    main()