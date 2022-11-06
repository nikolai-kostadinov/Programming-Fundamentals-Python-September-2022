def calc(number):
    if number == 1:
        a = int(input('Enter a:'))
        area = a * a
        print(area)
    elif number == 2:
        l = int(input('Enter l:'))
        w = int(input('Enter w:'))
        area = l * w
        print(area)
    elif number == 3:
        a = int(input('Enter a:'))
        b = int(input('Enter b:'))
        area = (a * b) / 2
        print(area)

number = int(input())
calc(number)

