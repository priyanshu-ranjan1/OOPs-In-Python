# gui made with ai

import tkinter as tk
from tkinter import messagebox

class Train:
    total_tickets = 100
    fare_per_ticket = 850

    def __init__(self, passenger_name, age, gender, no_of_tickets):
        self.passenger_name = passenger_name
        self.age = age
        self.gender = gender
        self.no_of_tickets = no_of_tickets

    def fare(self):
        fare = Train.fare_per_ticket
        if self.age < 18 or self.age > 60:
            fare *= 0.5  # 50% discount for minors and senior citizens
        elif self.gender.lower() == "male":
            fare = 100   # special flat fare for males
        return fare * self.no_of_tickets

    def book_ticket(self):
        if self.no_of_tickets <= Train.total_tickets:
            Train.total_tickets -= self.no_of_tickets
            return True, self.fare()
        else:
            return False, 0

# GUI Function
def book_now():
    name = entry_name.get()
    try:
        age = int(entry_age.get())
        gender = entry_gender.get()
        tickets = int(entry_tickets.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid age and ticket numbers.")
        return

    user = Train(name, age, gender, tickets)
    success, total_fare = user.book_ticket()
    if success:
        messagebox.showinfo("Booking Confirmed",
                            f"Ticket booked for {name}!\nTotal Fare: ₹{total_fare}\nTickets Left: {Train.total_tickets}")
    else:
        messagebox.showwarning("Booking Failed", "Not enough tickets available!")

# Build GUI
root = tk.Tk()
root.title("Indian Railways Ticket Booking")
root.geometry("400x450")
root.configure(bg="#f0f8ff")

tk.Label(root, text="🚆 Indian Railways Booking 🚆", font=("Arial", 16, "bold"), bg="#f0f8ff").pack(pady=15)

tk.Label(root, text="👤 Passenger Name:", bg="#f0f8ff").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="🎂 Age:", bg="#4d8fc9").pack()
entry_age = tk.Entry(root)
entry_age.pack()

tk.Label(root, text="🚻 Gender (male/female/other):", bg="#f0f8ff").pack()
entry_gender = tk.Entry(root)
entry_gender.pack()

tk.Label(root, text="🎫 Number of Tickets:", bg="#f0f8ff").pack()
entry_tickets = tk.Entry(root)
entry_tickets.pack()

tk.Button(root, text="🎟️ Book Ticket", command=book_now, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=25)

tk.Label(root, text="Tickets Remaining will be updated automatically.", bg="#f0f8ff", font=("Arial", 9)).pack()

root.mainloop()
