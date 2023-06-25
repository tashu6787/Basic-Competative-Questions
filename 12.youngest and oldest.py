person1= int(input("Enter your age: "))
person2= int(input("Enter your age: "))
person3= int(input("Enter your age: "))
if((person1 > person2) and (person1 > person3)):
    print(person1, "is the oldest")
elif((person2 > person1) and (person2 > person3)):
    print(person2, "is the oldest")
else:
    print(person3, "is the oldest")

if((person1 < person2) and (person1 < person3)):
    print(person1, "is the youngest")
elif((person2 < person1) and (person2 < person3)):
    print(person2, "is the youngest")
else:
    print(person3, "is the youngest")

   
