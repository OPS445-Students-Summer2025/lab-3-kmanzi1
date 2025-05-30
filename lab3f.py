#!/usr/bin/env python3

# Author ID: 183250232

my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    """Appends a new item to the end of the list with the value (last item + 1)."""
    ordered_list.append(ordered_list[-1] + 1)

def remove_items_from_list(ordered_list, items_to_remove):
    """Removes all values found in items_to_remove list from ordered_list."""
    for item in items_to_remove:
        if item in ordered_list:
            ordered_list.remove(item)

# Main code
if __name__ == '__main__':
    print(my_list)  # Expected output: [1, 2, 3, 4, 5]
    
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)  # Expected output: [1, 2, 3, 4, 5, 6, 7, 8]

    remove_items_from_list(my_list, [1, 5, 6])
    print(my_list)  # Expected output: [2, 3, 4, 7, 8]