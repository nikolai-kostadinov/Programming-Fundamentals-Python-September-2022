first_number = int(input())
second_number = int(input())
third_number = int(input())

def solve(first_number, second_number, third_number):
    min(first_number, second_number, third_number)
    return (first_number, second_number, third_number)

print(min(first_number, second_number, third_number))

