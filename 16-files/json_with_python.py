import json

# json.dumps is used to convert a list/dict to a JSON string - ENcoding

books = [
    {'title': 'The Gruffalo', 'author': 'Julia Donaldson'},
    {'title': 'The Twits', 'author': 'Roald Dahl'},
    {'title': 'he Bippolo Seed', 'author': 'Dr. Seuss'}
]

json_books = json.dumps(books)#encoding
print(json_books) #appears to be a list of dicts still but is actually a JSON string
print(type(json_books))#<class 'str'>

# json.loads is the opposite of dumps, used to convert a JSON string to a Python list/dict

decoded_books = json.loads(json_books)
print(decoded_books)

# using json module with file reading/writing:

# using file methods with a context manager to edit and return json:

with open("./widget.json") as widget_file:

    # read contents into a python dict
    a_dict = json.load(widget_file)
    print("\n\noriginal widget file:", a_dict)

    # make a change to the data:
    a_dict["widget"]["image"]["src"] = "Images/Moon.png"
    a_dict["widget"]["image"]["name"] = "moon1"
    a_dict["widget"]["text"]["onMouseUp"] = "moon1.opacity = (moon1.opacity / 100) * 90;"

# write modified python back to a new json file
with open("./modified-widget.json", mode="w") as modified_widget_file:

    # write the modified dict out to a new JSON file using the file handle in the new context manager above
    json.dump(a_dict, modified_widget_file)
