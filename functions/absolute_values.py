numbers = input().split(' ')
list = []

for num in numbers:
    list.append(abs(float(num)))

print(list)