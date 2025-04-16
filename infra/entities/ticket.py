
class ticket:
    # attributes: balance_hours, ticket_id, available_rides, expiry_duration
    def __init__(self):
        pass
    
    # balance hours attribute
    def get_balance_hours(self):
        return self.balance_hours
    def set_balance_hours(self, balance_hours):
        if type(balance_hours) != int:
            return "invalid input"
        else:
            self.balance_hours = balance_hours
            return self.balance_hours
    
    # ticket id attribute
    def get_ticket_id(self):
        return self.ticket_id
    def set_ticket_id(self, ticket_id):
        if type(ticket_id) != str:
            return "invalid input"
        else:
            self.ticket_id = ticket_id
            return self.ticket_id
    
    # available rides attribute
    def get_available_rides(self):
        return self.available_rides
    def set_available_rides(self, available_rides):
        if type(available_rides) != list:
            return "invalid input"
        else:
            self.available_rides = available_rides
            return self.available_rides
    
    # expiry duration attribute
    def get_expiry_duration(self):
        return self.expiry_duration
    def set_expiry_duration(self, expiry_duration):
        if type(expiry_duration) != int:
            return "invalid input"
        else:
            self.expiry_duration = expiry_duration
            return self.expiry_duration


    
