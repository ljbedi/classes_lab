from bus_stop import BusStop

class Bus:

    def __init__(self, route_number, destination):
        self.route_number = route_number 
        self.destination = destination 
        self.passengers = []


    def drive(self): 
        return "Brum Brum!"

    def passenger_count(self): 
        return len(self.passengers)
    
    def pick_up(self, name): 
        self.passengers.append(name)

    def drop_off(self, name):
        self.passengers.remove(name)

    def empty_bus(self):
        self.passengers.clear()

    def pick_up_from_stop(self, bus_stop):
        for passenger in bus_stop.queue:
            self.pick_up(passenger)
        bus_stop.clear()

        



