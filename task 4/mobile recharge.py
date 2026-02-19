Valid_plans = [199, 299, 399, 599]
def recharge(amount):
    return amount >= 50 and amount in Valid_plans
while True:
    recharge_amount = int(input("Enter the recharge amount: "))
    if recharge(recharge_amount):
        print("Recharge successful!")
        break  
    else:
        print("Invalid recharge amount. Please try again.")
    


