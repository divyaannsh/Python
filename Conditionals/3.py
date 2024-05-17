#Grade calculator

score = 112

if score >= 101:
    print("Please verify your grade again")
    exit()
if score >= 90:
    grade = "A"
elif score >= 80:
    grade ="B"
elif score >= 70:
    grade ="c"
elif score >= 60:
    grade ="d"

else:
    grade ="F"


print ("Grade", grade)