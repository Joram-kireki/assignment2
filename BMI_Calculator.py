# JORAM KIREKI SCT211-0079/2022

# Getting user's input
height = float(input("Enter your height in m:"))
weight = float(input("Enter your weight in kg:"))

# Defining BMI formula
BMI = weight/height**2

# Display BMI
print("Your Body Mass Index is:", BMI)

# Weight status
if BMI<= 18.5:
    print("Tough! You are underweight.")
elif BMI<= 24.9:
    print("Nice! You are at normal weight.")
else:
    print("Sheesh! You are overweight.")