def num(numbers):
    while True:
        command = input()

        if command == 'Finish':
            break
        if 'Replace' in command.split():
            command, product, new_number = command.split(' ')
        else:
            command, product = command.split(' ')

        if command == 'Add':
            numbers.append(product)
        elif command == 'Remove':
            if product in numbers:
                numbers.remove(product)
        elif command == 'Replace':
            if product in data:
                old_number_index = numbers.index(product)
                numbers.insert(old_number_index, new_number)
                numbers.remove(product)
        elif command == 'Collapse':
            for i in numbers:
                if i < product:
                    numbers.remove(i)


    print(' '.join(numbers))

data = input().split(' ')
num(data)



