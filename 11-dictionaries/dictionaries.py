'''
a dict is a mutable, unordered container of key: value pairs
keys must be unique, and, ideally, immutable (numbers or strings)
values may be duplicated
dicts are commonly used to represent complex data
and to facilitate sharing between different languages in any stack
eg. JavaScript > json > Python > json > Java
'''

book = {} # creation of empty dict possible as we can assign to it
book = dict()

# adding and updating props:

book['title'] = "Scary Smart" # actually adds a  key: value pair
book['author'] = "Mo Gawdat" # 
book['pub_year'] = 2019 # 

# getting dict values:
print(book['title'])

# various dict methods:
pub_year = book.pop('pub_year')#returns and removes last element (in order of declaration)
print(pub_year)
print(book)#{'title': 'Scary Smart', 'author': 'Mo Gawdat'} - mutated!

# iterating:
for key in book:#default is to return keys
    print(key)

for value in book.values():
    print(value)

for key, value in book.items():
    print(key, value)

# possible using keys to access values
for key in book:
    # print(book.key)# you absolutely cannot do this!
    # print(book[key])
    print(f"{key}: {book[key]}")