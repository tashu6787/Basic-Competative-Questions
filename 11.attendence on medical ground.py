held=int(input("Enter the no. of classes held: "))
attended= int(input("Enter the no. of classes attended: "))
percentage=attended*100/held
print("You have attended", percentage, "% of classes")
if(percentage <= 75):
    medical= input("Do you have a Medical reason Yes or No" )
    if(medical == "Yes"):
        print("You are allowed to sit in the examination")
    else:
        print("You are not allowed to sit in the examination")
else:
    print("You are allowed to sit in examination")
    
