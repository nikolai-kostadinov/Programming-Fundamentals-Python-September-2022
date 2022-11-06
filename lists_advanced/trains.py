number = int(input())
wagons = [0] * number
while True:
    command = input()

    if command == 'End':
        break

    split_command = command.split(' ')
    current_command = split_command[0]

    if current_command == 'add':
        people_to_add = int(split_command[1])
        wagons[-1] += people_to_add
     


