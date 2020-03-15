# ListComp will create a list in this case, by going through a dictionary and taking the keys
def create_list(some_list):
    return [element['name'] for element in some_list]

fruits = [
    {'name': 'avocado', 'price': 10},
    {'name': 'kiwi', 'price': 5},
    {'name': 'mango', 'price': 9},
]

print(create_list(fruits))

# DictComp will create a dictionary in the same way, this time, by taking the elements of a list
def create_dict(some_list):
    return {element[0] : element[1] for element in some_list}

more_fruits = [
    ['avocado', 10],
    ['banana', 1],
    ['papaya', 15]
]

print(create_dict(more_fruits))

