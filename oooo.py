import os

ticket_file = "tickets.txt"

def initialize_file():
    if not os.path.exists(ticket_file):
        with open(ticket_file, "w") as file:
            file.write("TrainNo,Name,Age,SeatNo\n")

def book_ticket(train_no, name, age, seat_no):
    with open(ticket_file, "a") as file:
        file.write(f"{train_no},{name},{age},{seat_no}\n")
    print("Ticket booked successfully!")

def view_tickets():
    with open(ticket_file, "r") as file:
        tickets = file.readlines()
    if len(tickets) <= 1:
        print("No tickets booked yet.")
        return
    print("Booked Tickets:")
    for ticket in tickets[1:]:
        print(ticket.strip())

def cancel_ticket(seat_no):
    with open(ticket_file, "r") as file:
        tickets = file.readlines()
    with open(ticket_file, "w") as file:
        file.write(tickets[0])  # Write header back
        found = False
        for ticket in tickets[1:]:
            details = ticket.strip().split(",")
            if details[3] == seat_no:
                found = True
                continue  # Skip writing this line to delete the ticket
            file.write(ticket)
    if found:
        print("Ticket cancelled successfully!")
    else:
        print("Ticket not found!")

def main():
    initialize_file()
    while True:
        print("\nRailway Ticket Booking System")
        print("1. Book Ticket")
        print("2. View Tickets")
        print("3. Cancel Ticket")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            train_no = input("Enter Train Number: ")
            name = input("Enter Passenger Name: ")
            age = input("Enter Age: ")
            seat_no = input("Enter Seat Number: ")
            book_ticket(train_no, name, age, seat_no)
        elif choice == "2":
            view_tickets()
        elif choice == "3":
            seat_no = input("Enter Seat Number to cancel: ")
            cancel_ticket(seat_no)
        elif choice == "4":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
