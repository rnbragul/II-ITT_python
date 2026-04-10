import re

def is_valid_gmail(email):
   # Pattern ensures it starts with letters/numbers/dots and ends exactly with @gmail.com
   pattern = r'^[a-zA-Z0-9._]+@gmail\.com$'
   return re.match(pattern, email) is not None

email = input("enter gmailID: ")
if is_valid_gmail(email):
   print("valid GMAIL")
else:
   print("invalid gmail")
