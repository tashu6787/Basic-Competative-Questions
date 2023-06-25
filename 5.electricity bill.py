units = int(input("Enter your electricity bill in units"))
if(units <= 100):
    print("0 is the total charge")
elif(units > 100 and units <= 200):
    print(((units - 100) * 5)," is the total charge")
else:
    print((((units - 100) * 5) + ((units - 200) * 10))," is the total charge")

