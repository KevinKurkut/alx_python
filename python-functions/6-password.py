def validate_password(password):
   if len(password) < 8:
        return False
   #check spaces
   if " " in password:
        return False
   upper = any(char.isupper() for char in password)
   lower = any(char.islower() for char in password)
   digit = any(char.isdigit() for char in password)

   return upper and lower and digit