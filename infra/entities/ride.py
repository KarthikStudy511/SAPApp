

class ride():
    # attribute: ride_name, ride_duration, min_age, max_age, ride_availability
    def __init__(self, ride_first_name, ride_duration, min_age, max_age, ride_no):
        self.ride_name = ride_first_name
        self.ride_duration = ride_duration
        self.min_age = min_age
        self.max_age = max_age
        self.ride_no= ride_no
        self.ride_availability = True
    
    
    # ride name attr
    def get_ride_name(self):
        return self.ride_name
    def set_ride_name(self, ride_name):
        
        self.ride_name = ride_name
    def get_ride_no(self):
        return self.ride_no

    # ride duration attr
    def get_ride_duration(self):
        return self.ride_duration
    def set_ride_duration(self, ride_duration):
        if type(ride_duration) != int:
            return "invalid input"
        else:
            self.ride_duration = ride_duration
            return self.ride_duration
    
    #ride minimum age attr
    def get_min_age(self):
        return self.min_age
    def set_min_age(self, min_age):
        if type(min_age) != int:
            return "invalid input"
        else:
            self.min_age = min_age
            return self.min_age
        
    #ride maximum age attr
    def get_max_age(self):
        return self.max_age
    def set_max_age(self, max_age): 
        if type(max_age) != int:
            return "invalid input"
        else:
            self.max_age = max_age
            return self.max_age
        
    # ride availability attr
    def get_ride_availability(self):
        return self.ride_availability
    def set_ride_availability(self, ride_availability):
        if type(ride_availability) != bool:
            return "invalid input"
        else:
            self.ride_availability = ride_availability
            return self.ride_availability

