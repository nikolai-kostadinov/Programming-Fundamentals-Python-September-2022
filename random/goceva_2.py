n = int(input())

def lipsum(data, n):
    index = 0
    for i in range(n) :
        word = data[index]
        if i%2==0:
            data.pop(i)
            data.insert(i,word.lower())
        else:
            data.pop(i)
            data.insert(i,word.upper())
        index += 1
    print(', '.join(data))

data = input().split(' ')
lipsum(data, n)