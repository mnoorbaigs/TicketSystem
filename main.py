# Call the ticket class from the ticket module (ticket.py)
from ticket import Ticket
# This function will create a new ticket
def create_ticket_interactively():
    """Function to create a ticket using user input."""
    print("Please provide the following information to create a new ticket:")
    staff_id = input("Enter Staff ID: ").strip()
    creator_name = input("Enter Ticket Creator Name: ").strip()
    contact_email = input("Enter Contact Email: ").strip()
    issue_description = input("Enter Description of the Issue: ").strip()

    # Create a new ticket with the provided details
    ticket = Ticket(staff_id, creator_name, contact_email, issue_description)
    print(f"\nTicket #{ticket.ticket_number} created successfully!\n")

# Main program
def main():
    while True:
        # Display options to the user
        print("Help Desk Ticketing System")
        print("1. Create a New Ticket")
        print("2. Display Tickets")
        print("3. Display Ticket Statistics")
        print("4. Exit")

        choice = input("Please select an option (1-4): ").strip()

        if choice == "1":
            create_ticket_interactively()
        elif choice == "2":
            print("\nPrinting Tickets:")
            Ticket.print_tickets()
        elif choice == "3":
            print("\nDisplaying Ticket Statistics")
            print(Ticket.ticket_statistics())
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the main program when the script is executed
if __name__ == "__main__":
    main()
