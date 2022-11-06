product_type = input()
product_quantity = int(input())

def solve(product_type, product_quantity):
    price = None
    if product_type == 'coffee':
        price = 1.5 * product_quantity
        return price
    elif product_type == 'coke':
        price = 1.4 * product_quantity
        return price
    elif product_type == 'water':
        price = 1 * product_quantity
        return price
    elif product_type == 'snacks':
        price = 2 * product_quantity
        return price

print(f'{solve(product_type, product_quantity):.2f}')

