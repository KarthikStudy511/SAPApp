
class customer:
    # attribtes: phone_no, player_name, player_age, spending_amt
    def __init__(self):
        pass

    # phone no of the player
    def get_phone_no(self):
        return self.phone_no
    def set_phone_no(self, phone_no):
        if type(phone_no) != str:
            return "invalid input"
        else:
            self.phone_no = phone_no
            return self.phone_no
    
    # name of the player
    def get_player_name(self):
        return self.player_name
    def set_player_name(self, player_name):
        if type(player_name) != str:
            return "invalid input"
        else:
            self.player_name = player_name
            return self.player_name
    
    # age of the player
    def get_player_age(self):
        return self.player_age
    def set_player_age(self, player_age):
        if type(player_age) != int:
            return "invalid input"
        else:
            self.player_age = player_age
            return self.player_age
    
    # spending amount of the player
    def get_spending_amt(self):
        return self.spending_amt
    def set_spending_amt(self, spending_amt):
        if type(spending_amt) != int:
            return "invalid input"
        else:
            self.spending_amt = spending_amt
            return self.spending_amt
    
    


