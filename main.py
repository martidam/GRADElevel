score = 49

grade = "F"

if  score >= 90:
    grade = "A"
elif score >= 80 and score < 90:
    grade = "B"
elif score >= 70 and score < 80:
    grade = "C"
elif score>= 60 and score < 70:
    grade = "D"
else score <= 60:
    grade = "F"

print("Your grade is ", grade)