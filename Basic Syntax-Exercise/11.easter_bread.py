budget = float(input())
price_per_1_kilo_flour = float(input())
current_bread_count = 0
colored_eggs_counter = 0
price_per_pack_of_eggs = price_per_1_kilo_flour * 0.75
price_for_liter_of_milk = price_per_1_kilo_flour * 1.25 / 4
one_bread_price = price_per_pack_of_eggs + price_for_liter_of_milk + price_per_1_kilo_flour

while budget >= one_bread_price:
    budget -= one_bread_price
    current_bread_count += 1
    colored_eggs_counter += 3
    if current_bread_count % 3 == 0:
        colored_eggs_counter -= current_bread_count -2

print(f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")


