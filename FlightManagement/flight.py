

class Flight: 
    # a dictionary to hold all available flights
    flights = {

        
    }
    def __init__(self, flight_number, destination, available_seats: list, departure_date, departure_time):
        self.flight_number = flight_number
        self.destination = destination 
        self.available_seats = available_seats 
        self.departure_date = departure_date 
        self.departure_time = departure_time 
    
    # a method to add flights 
    def add_flight(self): 
        Flight.flights[self.flight_number]= {
            'Destination': self.destination, 
            'Available Seats': self.available_seats, 
            'Departure Date': self.departure_date, 
            'Departure Time': self.departure_time, 
            'passengers': {

        }
        }
        print(f'flight number: {self.flight_number}, added\n')

    # show all flights available
    def all_flights(self): 
        if Flight.flights == {}:
              print('No Available Flights')
        else: 
            print('------------------------------------------')
            print('All Flights')
            print('------------------------------------------')
            for flight_id, flight_details in Flight.flights.items(): 
                print(f"Flight number:{flight_id}")
                print(f"Flight Destination: {flight_details['Destination']}")
                print(f"Available Seats: {flight_details['Available Seats']}")
                print(f"Departure Date: {flight_details['Departure Date']}")
                print(f"Departure Time: {flight_details['Departure Time']}")
                print(f"Passengers: {flight_details['passengers']}\n")


    # delete flight
    def delete_flight(self, flight_number): 
        if flight_number in Flight.flights.keys(): 
           Flight.flights.pop(flight_number)
           print('flight deleted')

# passenger class
class Passenger(Flight): 
    passengers = {}
    # bring the flights from the parent class 
    flights = Flight.flights 
    def __init__(self, name, passport_number, destination , age):
        self.name = name 
        self.passport_number = passport_number 
        self.destination = destination
        self.age = age 
    # add passenger to the list of all passengers 
    def add_passenger(self): 
        Passenger.passengers[self.name] = {
            'Name': self.name, 
            'Passport Number': self.passport_number, 
            'Age': self.age,
            'Destination': self.destination
        }
    # method to add a passenger to particular flight 
    def add_to_flight(self): 
        # adding passenger to a flight checking if there is a flight going to the destination and the seats are available
        for flight_number, details in Passenger.flights.items(): 
            if self.destination in details['Destination'] and len(details['Available Seats']) < 0: 
                details['passengers'][self.name] = {
                    'Name': self.name, 
                    'Passport Number': self.passport_number, 
                    'Age': self.age
                }
                 # removing one seat from the the number of available seats 
                details['Available Seats'].pop(0)
                print(f"you have been scheduled to fly to : {details['Destination']}")
          

    # showing all passengers regardless of destination 
    def all_passengers(self): 
        if Passenger.passengers == {}: 
            pass
        else: 
            print('---------------------------------------')
            print('All Passengers')
            print('---------------------------------------\n')
            for name, details in Passenger.passengers.items(): 
                print(f"Name:{name}")
                print(f"Passport Number:{details['Passport Number']}")
                print(f"Age:{details['Age']}")
                print(f"Destination:{details['Destination']}\n")
                








            


        
  

        


flight1 = Flight('B23421', 'Chicago', [1,2,3,4,5,6,7,8,9,10], '12-08-2024', '1:00pm')
flight2 = Flight('B23422', 'Arizona', [1,2,3,4,5,6,7,8,9,10], '12-08-2024', '2:00pm')


# calling deleting flight method
flight1.add_flight()
flight2.add_flight()

flight1.all_flights()

# flight1.delete_flight('B23421')



passenger1 = Passenger('Lechendem Stephen', 'B343213', 'Chicago', 29)
passenger2 = Passenger('Nkoambong Christina', 'B343564', 'Arizona', 29)


# adding passengers to a list of all passengers 
passenger2.add_passenger()
passenger1.add_passenger()

# adding passengers to a particular flight
passenger1.add_to_flight()

passenger1.all_passengers()


flight1.all_flights()



        

        