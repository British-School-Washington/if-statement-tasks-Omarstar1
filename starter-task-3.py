# Ask the user for their age
age = int(input("Enter your age: "))

# if the user is eligible to vote (age 18 or older)
if age >= 18:
    print("you can vot")

# if the user is not eligible to vote (under 18)
else:
    print("you cant vot")
