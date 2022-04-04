"""
Program Description : Write a program that calculates the total amount of a meal purchased
at restaurant .the program should ask the user to enter the charge for the food and amount
of 20% tip and %% tax.Display each amount in total
"""
quantity = int(input("No of meal purchased by customer: "))
rate = int(input("enter price per meal: "))
meal_amount = rate * quantity
tip = (20/100)*meal_amount
vat = (5/100)*meal_amount
total_amount = meal_amount + tip + vat
print("here is your receipt sir: ")
print(f"meal purchased = {quantity} \n"
      f"rate per meal = {rate} Rupees \n "
      f"amount = {meal_amount} Rupees \n"
      f" tip(20%) = {tip} Rupees \n"
      f" vat(5%)={vat} Rupees \n"
      f" grand total = {total_amount} Rupees")
