score = int(input("Insert your grade"))
if score >= 90:
    print("Your grade is A")
elif score >= 80:
    print("Your grade is B")
elif score >= 70:
    print("Your grade is D")
elif score >= 60:
    print("D")
elif score < 60:
    print("You failed")

# Car speed
Speed = int(input("What's your average speed?"))
Speed_allowed = int(input("What is your speed allowed"))
points = (Speed - Speed_allowed)/5

if Speed < 60 :
    print("OK")
else:
    if points < 12:
        print("Demerit points: " + str(points))
    else:
        print ("Go to jail")





