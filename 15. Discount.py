quantity= int(input("Enter the Quantity:"))
cost_of_quantity =100
purchase_amount=quantity*100
if(purchase_amount > 1000):
    Discount=purchase_amount/10
    Total=purchase_amount-Discount
    print("Total: ", Total)
else:
    Total=purchase_amount
    print("Total: ",Total)

