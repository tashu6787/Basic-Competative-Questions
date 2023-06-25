num=int(input("Enter  a  number"))
ldigit=num%10
print("Last digit is", ldigit)
if(ldigit % 3==0):
    print("Last digit is divisible by 3")
else:
    print("Last digit is not divisible by 3")
