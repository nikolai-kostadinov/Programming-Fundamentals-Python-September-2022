def odd_or_even(num):
    sum_of_odds = 0
    sum_of_even = 0
    for digit in num:
        if int(digit) % 2 == 0:
            sum_of_even += int(digit)
        else:
            sum_of_odds += int(digit)
    return sum_of_odds,sum_of_even

num_as_string = input()
sum_of_odds,sum_of_even = odd_or_even(num_as_string)
print(f'Odd sum = {sum_of_odds}, Even sum = {sum_of_even}')
