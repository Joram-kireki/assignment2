# JORAM KIREKI SCT211-0079/2022

# display welcome
print("Welcome to tip calculator")

# Get customer payment details
bill= float(input("What was the total bill? ksh:"))
tip = int(input("What percentage of the bill would you like to tip? 10, 12, or 15? "))
split = int(input("How many people are going to split the bill?"))

# Calculating the bill
total = bill * (1+(tip/100)) / split

# Display the bill
print(f"Your total is: ksh{total:.2f}")