# JORAM KIREKI SCT211-0079/2022

from datetime import datetime

# Getting date of birth
date_of_birth = input("Enter your birth date as: (dd mm yy)")

# Computing age
date_of_birth = datetime.strptime(date_of_birth,"%d %m %Y")
current_date = datetime.now()
difference = date_of_birth - current_date

days = difference.days
years = days // 365
months = days // 30

# display of age
print(f"Age in days: {days}")
print(f"Age in months: {months}")
print(f"Age in years: {years}")