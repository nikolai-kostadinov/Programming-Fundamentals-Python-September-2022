n = int(input())
numbers = []
filtered_numbers = []

for i in range(n):
    current_number = int(input())
    numbers.append(current_number)
command = input()
if command == 'even':
    for numbers in numbers:
        if numbers % 2 == 0:
            filtered_numbers.append(numbers)
elif command == 'odd':
    for numbers in numbers:
        if numbers % 2 != 0:
            filtered_numbers.append(numbers)
elif command == 'negative':
    for numbers in numbers:
        if numbers < 0:
            filtered_numbers.append(numbers)
elif command == 'positive':
    for numbers in numbers:
        if numbers >= 0:
            filtered_numbers.append(numbers)

print(filtered_numbers)

