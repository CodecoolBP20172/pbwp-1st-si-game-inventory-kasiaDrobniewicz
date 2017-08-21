# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

import csv

inv = {
    'arrow': 12,
    'gold coin': 42,
    'rope': 1,
    'torch': 6,
    'dagger': 1
}

inv2 = {
    'diamond': 2,
    'silver coin': 3
}

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

dragon_loot2 = ['gold coin', 'dagger', 'gold coin', 'diamond', 'ruby', 'diamond', 'diamond', 'silver coin']


# Displays the inventory.
def display_inventory(inventory):

    print ("Inventory: ")

    for key, value in inventory.items():
        print (value, key)

    print ("Total number of items: " + str(sum(inventory.values())))

print('Step 1 ------------------------------------------------')
display_inventory(inv)


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):

    for element in added_items:
    
        if element in inventory:
            inventory[element] = inventory[element] + 1

        else:
            inventory[element] = 1

    return inventory

print('Step 2 ------------------------------------------------')
inv_updated = add_to_inventory(inv, dragon_loot)
display_inventory(inv_updated)


# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):

    ADDITIONAL_SPACES = 3
    LEN_COUNT = 5
    LEN_ITEM_NAME = 9

    keys = list(inventory.keys())
 
    longest_key = max(keys, key=len)

    len_longest_key = len(longest_key)

    values = list(inventory.values())
 
    max_value = max(values)
 
    len_max_value = len(str(max_value))

    if LEN_ITEM_NAME > len_longest_key:
        len_longest_key = LEN_ITEM_NAME

    if LEN_COUNT > len_max_value:
        len_max_value = LEN_COUNT

    value_column_len = len_max_value + ADDITIONAL_SPACES
    
    number_of_spaces_count = value_column_len - LEN_COUNT

    key_column_len = len_longest_key + ADDITIONAL_SPACES

    number_of_spaces_item_name = key_column_len - LEN_ITEM_NAME

    print ('Inventory:')

    print (number_of_spaces_count * ' ' + 'count' + number_of_spaces_item_name * ' ' + 'item name')

    print((value_column_len + key_column_len) * '-')

    for key in keys:
        value = inventory[key]
    
        number_of_spaces_value = value_column_len - len(str(value))

        number_of_spaces_key = key_column_len - len(key)     

        print(number_of_spaces_value * ' ' + str(value) + number_of_spaces_key * ' ' + key)
 
    print((value_column_len + key_column_len) * '-')

    print ("Total number of items: " + str(sum(inventory.values())))


print('Step 3 ------------------------------------------------')
print_table(inv)


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):

    inventory.clear()
    
    with open(filename, 'r') as f_inv:
        reader = csv.reader(f_inv)
        list_of_items = list(reader)
        list_of_items = list_of_items[0]
    
    add_to_inventory(inventory, list_of_items)

    return inventory

print ('Step 4 ------------------------------------------------')
inv_from_file = import_inventory(inv, 'test_inventory.csv')
print_table(inv_from_file)


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    pass
