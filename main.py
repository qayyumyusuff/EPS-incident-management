def display_menu():
    print("=" * 40)
    print("EPS INCIDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Create Incident")
    print("2. View Incidents")
    print("3. Exit")


def main():
    display_menu()
    choice = input("Select an option: ")

    if choice == "1":
        print("Creating a new incident...")
    elif choice == "2":
        print("Viewing incidents...")
    elif choice == "3":
        print("Exiting...")
    else:
        print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()