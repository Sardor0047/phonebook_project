class Contact:
    first_name: str
    last_name: str
    phone_number: str
    def __init__(self,first_name:str,last_name:str,phone_number:str):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def check_phone_number(self):
        if len(self.phone_number) == 17 and self.phone_number[0] == '+' and self.phone_number.count(' ') == 4 and self.phone_number[4] == ' ' and self.phone_number[7] == ' ':
                return True
        return False
        
    def check_name(self):
        if self.first_name[0].isupper() and self.last_name[0].isupper():
            return True
        else :
            return False
a = Contact('Zarif','Naxalov','+998 93 123 45 67')