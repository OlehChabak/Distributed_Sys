import math
from datetime import datetime
from dateutil import parser

print("Hello world!")
Name = input ("Enter your name: ")
print("Hello,", Name)
NameLen = len(Name)
NameLenFac = math.factorial(NameLen)
print("Your name has", NameLen, "letters. Factorial of this number is", NameLenFac)

birth_date = parser.parse(input("Please, enter your birth date in format (DD.MM.YYYY):"))
age = today.year - date.year - ((today.month, today.day) < (date.month, date.day))
time_passed = date.today() - birth_date
print("Today is "+str(today.strftime('%d.%m.%y'))+", you are "+str(age)+" year old.(", time_passed,")")