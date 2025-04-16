from datetime import datetime, timedelta

class amusement_park:
    # attribtes: park_name, no_of_rides, per hour rate, opening time, closing time
    def __init__(self, opening_time):
        self.opening_time = opening_time
        self.closing_time = opening_time + timedelta(hours=8)

    # opening time attribute
    def set_opening_time(self, opening_time):
        
        if type(opening_time) != datetime:
            return "invalid input"
        else:
            self.opening_time = opening_time
            return self.opening_time
    def get_opening_time(self):
        return self.opening_time
    
    #closing time attribute
    def set_closing_time(self, closing_time):
        
        if type(closing_time) != datetime:
            return "invalid input"
        else:
            self.closing_time = closing_time
            return self.closing_time
    def get_closing_time(self):
        return self.closing_time

    # no of rides attribute
    def set_no_of_rides(self, no_of_rides):
        
        if type(no_of_rides) != int:
            return "invalid input"
        else:
            self.no_of_rides = no_of_rides
            return self.no_of_rides
    def get_no_of_rides(self):
        return self.no_of_rides
    
    # park name attribute
    def set_park_name(self, park_name):
        
        if type(park_name) != str:
            return "invalid input"
        else:
            self.park_name = park_name
            return self.park_name
    def get_park_name(self):
        return self.park_name

    # per hour rate attribute
    def get_per_hr_rate(self):
        return self.per_hr_rate
    def set_per_hr_rate(self, per_hr_rate):
        if type(per_hr_rate) != int:
            return "invalid input"
        else:
            self.per_hr_rate = per_hr_rate
            return self.per_hr_rate
    
    def get_working_hours(self):
        return int((self.get_closing_time() - self.get_opening_time()).total_seconds()) / 3600

