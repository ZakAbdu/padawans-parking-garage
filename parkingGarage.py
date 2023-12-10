# Start Your Code here

class ParkingGarage:
    def __init__(self, num_tickets, num_parking_spaces):
        self.tickets = list(range(1, num_tickets + 1))
        self.parkingSpaces = list(range(1, num_parking_spaces + 1))
        self.currentTicket = {}
    
    def takeTicket(self):
        if self.tickets:
            ticket_number = self.tickets.pop(0)
            parking_space = self.parkingSpaces.pop(0)
            self.currentTicket = {
                'Ticket_number': ticket_number, 
                'Parking_space': parking_space, 
                'Paid': False
            }
            print(f"Ticket #{ticket_number} issued. Parking space #{parking_space} has been reserved.")
        else:
            print('Sorry. No more tickets')
    
    def payForParking(self):
        user_payment = input('Enter payment amount: $')
        if user_payment:
            print(f"Ticket #{self.currentTicket['Ticket_number']} has been paid for. You have 15 minutes to leave.")
            self.currentTicket['Paid'] = True
    
    def leaveGarage(self):
        if self.currentTicket['Paid']:
            print('Thank you, have a nice day!')
        else:
            user_payment = input('Payment not received. Please enter payment amount: $')
            if user_payment:
                print(f"Ticket #{self.currentTicket['Ticket_number']} has been paid for. Thank you, have a nice day!")
                self.currentTicket['Paid'] = True
            else:
                print('Payment still not received. You not leaving till you pay up fool!')
            
            self.tickets.append(self.currentTicket['Ticket_number'])
            self.parkingSpaces.append(self.currentTicket['Parking_space'])
            self.currentTicket = {}


garage = ParkingGarage(10,10)
garage.takeTicket()
garage.payForParking()
garage.leaveGarage()