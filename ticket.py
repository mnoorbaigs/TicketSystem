# Below class represents to support tickets
class Ticket:
    counter = 0  # Class attribute to keep track of total tickets created
    tickets_list = []  # Class attribute to store all created ticket objects

    # THis will construct to initialization a ticket
    def __init__(self, staff_id, creator_name, contact_email, issue_description):
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.issue_description = issue_description
        self.ticket_number = Ticket.counter + 2000  # Assign a unique ticket number
        Ticket.counter += 1  # Increment the counter
        self.response = "Not Yet Provided"  # Initialize response
        self.status = "Open"  # Initialize status as "Open"
        Ticket.tickets_list.append(self)  # Add the created ticket to the list of tickets

    # This will generate new password and close the ticket
    def generate_password(self):
        new_password = self.staff_id[:2] + self.creator_name[:3]
        self.response = f"New Password Generated: {new_password}"
        self.close_ticket()

    # This will provide a respinse and close the ticket accordingly
    def provide_response(self, response):
        self.response = response
        self.close_ticket()

    # the below method will close the ticket.
    def close_ticket(self):
        self.status = "Closed"

    # This method will reopen a closed ticket
    def reopen_ticket(self):
        self.status = "Reopened"

    # This method will print information for all created tickets
    @classmethod
    def print_tickets(cls):
        for ticket in cls.tickets_list:
            print(f"Ticket Number: {ticket.ticket_number}")
            print(f"Ticket Creator: {ticket.creator_name}")
            print(f"Staff ID: {ticket.staff_id}")
            print(f"Email Address: {ticket.contact_email}")
            print(f"Description: {ticket.issue_description}")
            print(f"Response: {ticket.response}")
            print(f"Ticket Status: {ticket.status}")
            print(" ")

    # This method will provide ticket statistics
    @classmethod
    def ticket_statistics(cls):
        tickets_created = cls.counter
        tickets_resolved = sum(1 for ticket in cls.tickets_list if ticket.status == "Closed")
        tickets_to_solve = tickets_created - tickets_resolved
        return f"Ticket Created{tickets_created}\nTicket Resolved:{tickets_resolved}\nTicketTo Solve:{tickets_to_solve}"
