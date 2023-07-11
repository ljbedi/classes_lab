

class BusStop:
    
    def __init__(self, name):
        self.name = name 
        self.queue = []

    def add_to_queue(self, name):
        self.queue.append(name)

    def remove_person_from_queue(self, name):
        self.queue.clear(name)

    def clear(self):
        self.queue.clear()

    def queue_length(self):
        return len(self.queue)


# people at stop 
# people get on bus
# list at stop clear 
# people on bus 
# empty the bus 


#  REMOVE FROM QUEUE
# ADD TO PASSENGERS 
