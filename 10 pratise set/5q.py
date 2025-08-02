'''
#Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Indian Railways.
class Train: total_tickets=100 ticket_availability=True def init(self,username,age,gender,no_of_tickets): self.username=username self.age=age self.gender=gender self.no_of_tickets=no_of_tickets

'''
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
            fare *= 0.5  # 50% discount for students/kids and elders 
        elif self.gender.lower() == "male":
            fare = 100  # special boy discount 

        return fare * self.no_of_tickets

    def book_ticket(self):
        if self.no_of_tickets <= Train.total_tickets:
            Train.total_tickets -= self.no_of_tickets
            print(f"\n Ticket booked for: {self.passenger_name}")
            print(f" Total Fare: ₹{self.fare()}")
        else:
            print("\n Not enough tickets available!")

    def status(self):
        print(f" Tickets left: {Train.total_tickets}")
        if Train.total_tickets > 0:
            print(" Tickets available")
        else:
            print(" No tickets left")


#  Taking inputs
passenger_name = input(" Enter passenger name: ")
age = int(input(" Enter age: "))
gender = input(" Enter gender (male/female/other): ")
tickets = int(input(" How many tickets to book? "))

#  Creating object with inputs
user1 = Train(passenger_name, age, gender, tickets)

#  Booking and showing details
user1.book_ticket()
user1.status()
