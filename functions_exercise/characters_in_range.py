char_1 = input()
char_2 = input()
def solve(first, second):
    characters = []
    for char in range(ord(first) + 1, ord(second)):
        characters.append(chr(char))
    return characters
result = solve(char_1, char_2)
print(' '.join(result))

