import json

# dumps (dump str) is used to convert a list/dict to a JSON string
books = [
    {'title': 'The Gruffalo', 'author': 'Julia Donaldson'},
    {'title': 'The Twits', 'author': 'Roald Dahl'},
    {'title': 'he Bippolo Seed', 'author': 'Dr. Seuss'}
]
json_books = json.dumps(books)
print(json_books) # looks like a list of dicts still but is a JSON string
print(type(json_books)) #<class 'str'>
'''
[{"title": "The Gruffalo", "author": "Julia Donaldson"}, {"title": "The Twits", "author": "Roald Dahl"}, {"title": "The Bippolo Seed", "author": "Dr. Seuss"}]
'''
# ---

# loads (load str) is the opposite of dumps; is used to convert a JSON string to a list/dict
books = json.loads(json_books)
print(books)
# [{'title': 'The Gruffalo', 'author': 'Julia Donaldson'}, {'title': 'The Twits', 'author': 'Roald Dahl'}, {'title': 'The Bippolo Seed', 'author': 'Dr. Seuss'}]
print(type(books)) # <class 'list'>

# ---

# the dump and load functions are the same but write to and read from JSON files

with open("./widget.json") as widget_file:

    # read the contents of widget.json into a dict
    a_dict = json.load(widget_file)
    print("original widget file", a_dict)

    # make a change to the data
    a_dict["widget"]["image"]["src"] = "Images/Moon.png"
    a_dict["widget"]["image"]["name"] = "moon1"
    a_dict["widget"]["text"]["onMouseUp"] = "moon1.opacity = (moon1.opacity / 100) * 90;"

with open("./modified-widget.json", mode="w") as modified_widget_file:

    # write the modified dict out to a new JSON file
    json.dump(a_dict, modified_widget_file)

# ad hoc below here
with open("./modified-widget.json") as modified_widget_file:
    a_dict_mod = json.load(modified_widget_file)
    print("modified widget file", a_dict_mod)
