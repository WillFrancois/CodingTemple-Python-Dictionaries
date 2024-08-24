#Task 1
tickets = {"TKT1": {"Requested By":"Thomas", "Ticket Type":"Incident", "Status":"Open"},
           "TKT2": {"Requested By": "Emily", "Ticket Type":"Request", "Status":"Closed"}
          }

def create_ticket(requested_by, ticket_type, status):
    tickets["TKT" + str(len(tickets) + 1)] = {"Requested By":requested_by, "Ticket Type": ticket_type, "Status": status}

def update_ticket(ticket_number, status):
    tickets[ticket_number]["Status"] = status

def display_tickets(ticket_type="all"):
    if ticket_type == "all":
        for ticket in tickets:
            print(ticket + ": ", tickets[ticket])
    else:
        for ticket in tickets.values():
            if ticket["Ticket Type"] == ticket_type:
                print(ticket)

def input_escape(message):
    provided_input = input(message)
    if provided_input == 'q':
        exit()
    else:
        return provided_input

def main_menu():
    user_inp = input_escape("Please provide a command for this ticketing system:\n1. Create ticket\n2. Update ticket\n3. Display ticket\nInput q to quit this program.\n")

    while True:
        match user_inp:
            case '1':
                print()
                rb = input_escape("Who was this ticket requested by? ")
                tt = input_escape("Is this an incident or request? ")
                s = input_escape("Is this ticket open or already closed? ")

                tt = "Incident" if len(tt) > 0 and tt[0] in ["i", "i"] else "Request"
                s = "Closed" if len(s) > 0 and s[0] in ["C", "c"] else "Open"
                create_ticket(rb, tt, s)
                print()

            case '2':
                print()
                display_tickets()
                print()
                tkt_num = input_escape("Which ticket would you like to open or close? ")
                print()
                
                try:
                    tickets[tkt_num]["Status"] = "Open" if tickets[tkt_num]["Status"] == "Closed" else "Closed"
                except KeyError:
                    print("Ticket number not found!")

            case '3':
                tkt_type = input_escape("\nWhat type of tickets would you like to see? (Incident or Request) ")
                tkt_type = "Incident" if len(tkt_type) > 0 and tkt_type[0] in ["i", "I"] else tkt_type
                tkt_type = "Request" if len(tkt_type) > 0 and tkt_type[0] in ["r", "R"] else "all"
                print()
                display_tickets(tkt_type)
                print()

        user_inp = input_escape("Please provide a command for this ticketing system:\n1. Create ticket\n2. Update ticket\n3. Display ticket\nInput q to quit this program.\n")

main_menu()
