incidents = []

def display_menu():
    print("=" * 40)
    print("EPS INCIDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Create Incident")
    print("2. View Incidents")
    print("3. Exit")

def create_incident():

    
    print("\nCreate New Incident")
    print("-" * 40)


    date = input("Date: ")
    incident_time = input("Incident time: ")
    incident_description = input("Incident description: ")
    sap_number = input("SAP number: ")
    location = input("Location: ")
    response_time = input("Response time: ")
    duration = input("Duration: ")


    print("\nIncident Summary")
    print("-" * 40)
    print(f"Date: {date}")
    print(f"Incident Time: {incident_time}")
    print(f"Incident Description: {incident_description}")
    print(f"SAP Number: {sap_number}")
    print(f"Location: {location}")
    print(f"Response Time: {response_time}")
    print(f"Duration: {duration}")


    incident ={
            "date": date,
            "incident_time": incident_time,
            "incident_description": incident_description,
            "sap_number": sap_number,
            "location": location,
            "response_time": response_time,
            "duration": duration,
        }
    
    
    incidents.append(incident)

def view_incidents():
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
        print(f"Duration: {incident['duration']}")
        print("-" * 40)

            
def main():
    while True:
        display_menu()
        choice = input("Select an option: ")


        if choice == "1":
            create_incident()

        elif choice == "2":
            view_incidents()
            
        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")     

        print() 


if __name__ == "__main__":
    main()