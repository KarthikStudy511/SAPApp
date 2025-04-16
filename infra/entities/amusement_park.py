class amusement_park:
    # attribtes: opening time, closing time, ride_no, park_name
    def __init__(self):
        pass
    def set_opening_time(self, opening_time):
        self.opening_time = opening_time
        if type(self.opening_time) == str:
            return "invalid input"
        else:
            return self.opening_time
    def get_opening_time(self):
        
        return self.opening_time
    def get_closing_time(self):
        return self.closing_time
    def set_closing_time(self, closing_time):
        self.closing_time = closing_time
        if type(self.closing_time) == str:
            return "invalid input"
        else:
            return self.closing_time

    def set_ride_no(self, ride_no):
        self.ride_no = ride_no
        if type(self.ride_no) == str:
            return "invalid input"
        else:
            return self.ride_no


