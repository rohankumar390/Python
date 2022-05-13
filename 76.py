# def searcher():
#     import time
#     book="This is a book on harry and code with harry and good"
#     time.sleep(4)

#     while True:
#         text=(yield)
#         if text in book:
#             print("Your text is in the book")
#         else:
#             print("Text is not in the book")

# search = searcher()
# print("search started")
# next(search)


# once closed cannot be open corotine


def searcher():
    import time
    book = []
    time.sleep(4)
    print("Enter the coroutine you want to add")
    for i in range(5):
        user = input()
        book.append(user)

    while True:
        text = (yield)
        if text in book:
            print("Your text in the book.")

        else:
            print("Text is not in the book")

search = searcher()
print("search started")
next(search)
print("Next method running")
print("Enter your name")
searching = input()
search.send(searching)