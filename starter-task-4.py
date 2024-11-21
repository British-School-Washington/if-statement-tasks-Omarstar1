# Ask the user to enter their score (0-100)
score = int(input("Enter your score: "))

# if the score is 90 or above
if score >= 90:
    grade = "A"

# if the score is between 80 and 89
elif score >= 80:
    grade = "B"

# if the score is between 70 and 79
elif score >= 70:
    grade = "C"

# if the score is below 70
else:
    grade = "FAIL!!!!"

print(f"You got a",grade)
