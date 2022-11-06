operator = input()
first_num = int(input())
second_num = int(input())

def solve(a,b,operator):
    result = None
    if operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return int(a / b)
    elif operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b
    return result

print(solve(first_num, second_num, operator))



