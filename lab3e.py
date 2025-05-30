#!/usr/bin/env python3

# Author ID: 183250232

my_list = [100, 200, 300, 'six hundred']

def give_list():
    return my_list  # Returns all items unchanged

def give_first_item():
    return str(my_list[0])  # Converts the first item to a string before returning

def give_first_and_last_item():
    return [my_list[0], my_list[-1]]  # Returns a new list with the first and last items

def give_second_and_third_item():
    return my_list[1:3]  # Returns a new list with the second and third items

if __name__ == '__main__':
    print(give_list())  # Expected output: [100, 200, 300, 'six hundred']
    print(give_first_item())  # Expected output: '100'
    print(give_first_and_last_item())  # Expected output: [100, 'six hundred']
    print(give_second_and_third_item())  # Expected output: [200, 300]