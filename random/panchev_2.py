figure = int(input())
def square():
    a = int(input('Enter a:'))
    area_1 = a * a
    print(f'The area of the square is: {area_1}')
def rectangle():
    a = int(input('Enter a:'))
    b = int(input('Enter b:'))
    area_2 = a * b
    print(f'The area of the rectangle is: {area_2}')
def triangle():
    a = int(input('Enter a:'))
    b = int(input('Enter b:'))
    area_3 = (a * b) / 2
    print(f'The area of the triangle is: {area_3}')

if figure == 1:
    square()
elif figure == 2:
    rectangle()
elif figure == 3:
    triangle()

