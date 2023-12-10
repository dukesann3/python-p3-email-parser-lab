# your code goes here!
import re

class EmailAddressParser:

    def __init__(self, email_addresses):
        self.email_addresses = email_addresses
    
    def parse(self):
        acceptable_email = r"[a-zA-Z^\.]+@[a-zA-Z0-9]+.com"
        email_regex = re.compile(acceptable_email)
        email_address_list = re.findall(email_regex, self.email_addresses)
        sorted_email_address_list = sorted(email_address_list)
        return sorted_email_address_list
        

new_address_list = EmailAddressParser("talk@talk.com john.jones@flatironschool.com alexa@amazon.com")
print(new_address_list.parse())


