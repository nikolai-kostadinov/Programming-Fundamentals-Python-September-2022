number_of_lines = int(input())
list1 = []
list2 = []
count_positive = 0
sum_negative = 0
for i in range(number_of_lines):
    numbers = int(input())
    if numbers >= 0:
        list1.append(numbers)
        count_positive += 1
    else:
        sum_negative += numbers
        list2.append(numbers)
print(f'{list1}\n'
      f'{list2}\n'
      f'Count of positives: {count_positive}\n'
      f'Sum of negatives: {sum_negative}')