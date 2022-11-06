list = []
number_of_numbers = int(input())

for lines in range(number_of_numbers):
    sum_of_digits = 0
    numbers = int(input())
    list.append(numbers)
for digit in str(numbers):
    sum_of_digits += int(digit)
sum_of_numbers = 0
for numbers in list:
    if int(sum_of_digits) % 2 == 0:
        sum_of_numbers = sum(list)
    if int(sum_of_digits) % 2 != 0:
            list.remove(numbers)
print(list)
print(sum_of_numbers)

