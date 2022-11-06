def library(shelf):
    while True:
        command = input()

        if command == 'Done':
            break

        if 'Swap Books' in command.split():
            command,book_1,book_2 = command.split(' | ')
        else:
            command, product = command.split(' | ')

        if command == 'Add Book':
            if product in data:
                pass
            else:
                shelf.insert(0,product)

        elif command == 'Take Book':
            if product in data:
                shelf.remove(product)
            else:
                pass
        elif command == 'Swap Books':
            if book_1 in data and book_2 in data:
                book_1_index = shelf.index(book_1)
                book_2_index = shelf.index(book_2)
                shelf.insert(book_2_index, book_1)
                shelf.remove(book_2)
                shelf.insert(book_1_index, book_2)
                shelf.remove(book_1)
            else:
                pass
        elif command == 'Insert Book':
            if product in data:
                pass
            else:
                shelf.append(product)
        elif command == 'Check Book':
            if int(product) <= len(shelf) :
                print(shelf.index(int(product)))



    print(', '.join(shelf))

data = input().split('&')
library(data)