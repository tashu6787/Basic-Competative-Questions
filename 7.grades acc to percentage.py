percentage= float(input("Enter your percentage: "))
if(percentage > 90):
    print("Your grade is A")
elif( percentage > 80 and percentage <= 90):
    print("Your grade is B")
elif( percentage >= 60 and percentage <= 80):
    print("Your grade is C")
else:
    print("Your grade is D")
