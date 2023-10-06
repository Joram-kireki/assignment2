# JORAM KIREKI SCT211-0079/2022

"""A leap year is any year exactly divisible by 4 except for century years (years ending with 00).
The century year is a leap year only if it is perfectly divisible by 400."""

# Getting the year from the user
year = int(input("Enter the year:"))


if (year%4)==0:
    if (year%100)==0:
        if (year%400)==0:
            print(year,"is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year,"is a leap year.")
else:
    print(year,"is not a leap year")
    