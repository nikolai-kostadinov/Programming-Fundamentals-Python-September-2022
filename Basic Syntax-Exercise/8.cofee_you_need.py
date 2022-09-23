command = input()
coffes = 0
while command != 'END':
    if command == 'dog' or command == 'cat' or command == 'coding' or command == 'movie':
        coffes += 1
    elif command == 'DOG' or command == 'CAT' or command == 'CODING' or command == 'MOVIE':
        coffes += 2
    command = input()

if coffes > 5:
    print('You need extra sleep')
else:
    print(coffes)