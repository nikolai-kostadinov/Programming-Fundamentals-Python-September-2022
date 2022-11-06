number_of_cities = int(input())
profit = 0
total = 0
for i in range(1,number_of_cities + 1):
    name_of_city = str(input())
    income = float(input())
    expenses = float(input())

    if i % 3 == 0:
        if i % 5 != 0:
            expenses += 0.5 * expenses
    if i % 5 == 0:
        income -= 0.1 * income
    profit += income - expenses
    total += profit
    print(f'In {name_of_city} Burger Bus earned {profit:.2f} leva.')
    profit = 0
print(f"Burger Bus total profit: {total:.2f} leva.")




