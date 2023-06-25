salary= float(input("Enter your salary: "))
service= int(input("Enter your year of service: "))
if(service > 5):
    bonus= 5*salary/100
    total_salary= salary + bonus
    print("you get a bonus of", bonus, "and your total salary is", total_salary)
else:
    print("you don't get any bonus so your total salary is", salary)
