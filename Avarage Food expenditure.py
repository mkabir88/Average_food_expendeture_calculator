#The program asks the user how many times a week they eat at the student cafeteria.
#Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.
#Based on this information the program calculates the user's typical food expenditure both weekly and daily.
#Version1

times_eating_in_cafe = int(input("How many times a week do you eat at the student cafeteria?: "))
lunch_price = float(input("The price of a typical student lunch?: "))
groceroes = float(input("How much money do you spend on groceries in a week?: "))
cost_of_cafe = (times_eating_in_cafe * lunch_price)

print("Average food expenditure:")
print(f"Daily: {(cost_of_cafe + groceroes) / 7} euros")
print(f"Weekly: {cost_of_cafe + groceroes} euros")
