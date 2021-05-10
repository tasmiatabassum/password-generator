import random
from password_strength import PasswordStats

def shuffle(string):
    temporarylist = list(string)
    random.shuffle(temporarylist)
    return ''.join(temporarylist)
#password elements
# min length: 8 
#need min. 2 uppercase letters
# need min. 2 digits
# need min. 2 special characters
# need min. 2 non-letter characters (digits, specials, anything)
   
uppercase_letter1 = chr(random.randint(65,90))
uppercase_letter2 = chr(random.randint(65,90))
uppercase_letter3 = chr(random.randint(65,90))
uppercase_letter4 = chr(random.randint(65,90))
uppercase_letter5 = chr(random.randint(65,90))
uppercase_letter6 = chr(random.randint(65,90))
lowercase_letter1 = chr(random.randint(97,122))
lowercase_letter2 = chr(random.randint(97,122))
lowercase_letter3 = chr(random.randint(97,122))
lowercase_letter4 = chr(random.randint(97,122))
digit1 = chr(random.randint(48,57))
digit2 = chr(random.randint(48,57))
digit3 = chr(random.randint(48,57))
digit4 = chr(random.randint(48,57))
symbol1 = chr(random.randint(32,152))
symbol2 = chr(random.randint(32,152))
symbol3 = chr(random.randint(32,152))
symbol4 = chr(random.randint(32,152))

#generating the password
password = uppercase_letter1 +symbol3+ uppercase_letter2 + symbol4+lowercase_letter1 +digit3 +lowercase_letter2 +lowercase_letter3+uppercase_letter3 + uppercase_letter4 +lowercase_letter4+ digit1 + digit2 + uppercase_letter5 + symbol1 +digit4+uppercase_letter6 +symbol2
password = shuffle(password)

print('Here is your generated password: ', password)

#checking strength
print("Password strength ranges from  0.00 to 0.99, strong passwords start at 0.66.")
print("Your password strength is : ", stats.strength())

