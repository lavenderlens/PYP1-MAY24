# sometimes you may want to raise an exception yourself
# why? New devs generally resent spending time fixing the ones they already get!
# Because sometimes stopping or pausing script execution is preferable to the alternatives
# if you are creating objects your business logic may impose rules
# if these rules are flouted, then invalid objects get into the system

import BookError

books = [] # mutable

num_books = 0

def add_new_book(title, fname, lname):
    # we don't want books with an author fname or lname < 2 characters
    if len(fname.strip()) <2 or len(lname.strip()) <2:
        raise BookError("The book's author first and last names must be two characters o longer")
    else:
        book = {"title": title, "first name": fname, "last name": lname}
        books.append(book)
        global num_books
        num_books += 1

add_new_book("Why We drive", "Matthew", "Crawford")
add_new_book("Scary Smart", "Mo", "Gawdat")
try:
    add_new_book("Scary", "X", "Y")
except:
    print("book not created")

print(books)#the dodgy business logic did NOT result in a book object being created with invalid fields
