n = int(input())
word = input()
list = []

for i in range(n):
    current_strings = input()
    list.append(current_strings)
print(list)
for i in range(len(list) -1,-1,-1):
    element = list[i]
    if word not in element:
        list.remove(element)
print(list)
