#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Michael Alonso
Class: CS 521 - Spring 1
Date: 03/03/2020
Final Project
Program that uses class CoffeeShops to create, edit, and store in files
an inventory of coffee shops
"""
# Import
from CoffeeShops import CoffeeShops
import sys
import os.path


# Begin Functions used in program
def validate_file(file_name):
    '''
    This function will validate that the passed file exists and returns
    a boolean value
    '''
    return os.path.isfile(file_name)


def validate_integer():
    '''
    This function will validate that an integer was entered into input for a
    menu selection loop and returns a valid integer input
    '''
    # Validating input is integer
    while True:
        try:
            user_input = input('Enter your selection here: ')
            user_input = int(user_input)
            break
        except:
            print('The option entered isn\'t valid, please try again:')

    return user_input


def write_file(file_name, inventory_list):
    '''
    This function will write objects from the class CoffeeShops
    to the passed file and does not return a value
    '''
    open_file = open(file_name, "w")
    # Writing to file
    for x in range(len(inventory_list)):
        open_file.write(str(inventory_list[x].get_name()).upper() + ",")
        open_file.write(str(inventory_list[x].get_city()).upper() + ",")
        open_file.write(str(inventory_list[x].get_rank()) + ",")
        open_file.writelines(str(inventory_list[x].get_favorite_drink()).upper())

    open_file.close()


def append_file(file_name, entry_list):
    '''
    This function will append objects from class CoffeeShops to the passed
    file name and will return a confirmation string when entry has been added
    '''
    # Writing entry with commas to easily retrieve lists from file
    open_file = open(file_name, "a")
    open_file.write(str(entry_list[0].strip()).upper() + ",")
    open_file.write(str(entry_list[1].strip()).upper() + ",")
    open_file.write(str(entry_list[2]) + ",")
    open_file.write(str(entry_list[3].strip()).upper())
    open_file.write('\n')
    open_file.close()
    return 'Entry has been added to the inventory.'


def read_file(file_name):
    '''
    This function will read the passed file and return a nested list
    '''
    # Reading file and making a nested list variable
    with open(file_name, "r") as open_file:
        inventory_list = [[name for name in line.split(',')]
                          for line in open_file]
    open_file.close()
    return inventory_list


def get_index_number(coffee_list, name):
    '''
    This function checks to see if a value is in the passed object list
    from class CoffeeShops and returns the integer index position and
    boolean value
    '''
    # Define variables
    present = False
    index = None

    # Searching object list for a match to passed argument name
    for x in range(len(coffee_list)):
        if name == coffee_list[x].get_name():
            index = x
            present = True

    return index, present


if __name__ == '__main__':

    # Declare Variables
    FILE = 'Inventory.txt'
    inventory_list = []
    coffee_list = []
    sorted_coffee_list = []
    user_input = -1
    ENTRY_SIZE = 4
    present = False

    # Calling function to get boolean value to see if FILE exists
    file_exist = validate_file(FILE)

    # Based on file_exist boolean value, will either read or create file
    if file_exist is True:
        inventory_list = read_file(FILE)
    else:
        write_file(FILE, inventory_list)

    # Creating CoffeeShops objects and appending to list coffee_list
    for x in range(len(inventory_list)):
        coffee_list.append(CoffeeShops(str(inventory_list[x][0]).upper(),
                                       str(inventory_list[x][1]).upper(),
                                       int(inventory_list[x][2]),
                                       str(inventory_list[x][3]).upper()))

    # Present menu
    while True:
        while user_input != 0:

            # Display menu choices
            print('{0:15.0s} Coffee Inventory Menu'.format(' '))
            print('\tEnter 1 to Add a new Coffee Shop Entry')
            print('\tEnter 2 to Update a Coffee Shop Entry')
            print('\tEnter 3 to Remove a Coffee Shop Entry')
            print('\tEnter 4 to View Coffee Shop Inventory')
            print('\tEnter 5 to View your Top Five Coffee Shops')
            print('\tEnter 6 to Find a Coffee Shop Entry by name')
            print('\tEnter 0 to Exit the menu')

            # Validate input is integer
            user_input = validate_integer()
            break

        # Start if statement to process menu selection
        # Adding new entry
        if user_input == 1:

            # Getting values for entry
            while True:
                entry_list = input("Enter name, city, rank "
                                   "(with 1 being the best),"
                                   " and favorite drink separated by "
                                   "a comma: ").split(',')

                # Validating length of entry
                while len(entry_list) != ENTRY_SIZE:
                    if len(entry_list) != ENTRY_SIZE:
                        print("You didn\'t enter {0}. Please try again.".
                              format(ENTRY_SIZE))
                        entry_list = input("Enter name, city, rank "
                                           "(with 1 being the best), "
                                           "and favorite drink separated by "
                                           "a comma: ").split(',')

                # Validating Rank is integer value
                try:
                    entry_list[2] = int(entry_list[2])
                    break
                except:
                    print('{} is not an integer. Please try again'.
                          format(entry_list[2]))

            # Validating Rank is positive number greater than zero
            if entry_list[2] < 1:
                print("{} is not a valid integer. "
                      "Enter an integer greater than 0".format(entry_list[2]))
                sys.exit()

            # Appending new class object to list
            coffee_list.append(CoffeeShops(entry_list[0].strip().upper(),
                                           entry_list[1].strip().upper(),
                                           entry_list[2],
                                           entry_list[3].strip().upper()))

            # Calling function to append to file
            result = append_file(FILE, entry_list)

            # Printing confirmation to console
            print(result)

        # Update coffee shop
        elif user_input == 2:
            # Call to function to update shop info
            # Get name of coffee shop
            name = input("Enter the name of the coffee shop "
                         "to update: ").strip().upper()

            # Call to function to return list index position and boolean value
            index, present = get_index_number(coffee_list, name)

            # Validating coffee shop name is in coffee_list
            if present is False:
                print('Invalid shop name. Please try again.')
                sys.exit()

            # Menu for updating entries
            while True:
                print('\tEnter 1 to change the Name of the coffee shop')
                print('\tEnter 2 to change the Rank of the coffee shop')
                print('\tEnter 3 to change the Favorite Drink of the coffee shop')
                print('\tEnter 4 to change the City of the coffee shop')

                # Call to validate selection choice
                user_input = validate_integer()
                break

            # If statements to navigate menu and to update entries by index
            # Update Name
            if user_input == 1:
                update = input('Enter a new name: ').strip().upper()

                # Updating class object
                coffee_list[index].update_shop(1, update)

            # Update Rank
            elif user_input == 2:

                # Validating input for positive integer greater than 1
                while True:
                    update = input("Enter a new rank, with 1 being the "
                                   "best: ").strip().upper()
                    try:
                        update = int(update)
                        break
                    except:
                        print('Rank not integer. Please try again.')

                if update < 1:
                    print("{} is not a valid integer. "
                          "Enter an integer greater than 0".format(update))
                    sys.exit()

                # Updating class object
                coffee_list[index].update_shop(2, update)

            # Update Favorite Drink
            elif user_input == 3:
                update = input("Enter a new favorite "
                               "drink: ").strip().upper()

                # Updating class object
                coffee_list[index].update_shop(3, update + '\n')

            # Update City
            elif user_input == 4:
                update = input("Enter a new city: ").strip().upper()
                # Updating class object
                coffee_list[index].update_shop(4, update)

            else:
                print('You didn\'t enter a valid option.\n')
                sys.exit()

            # Calling function to write updates to file
            write_file(FILE, coffee_list)

            # Printing confirmation to console
            print('{0} has been updated'.format(name))

        # Remove coffee shop
        elif user_input == 3:
            name = input("Enter the name of the coffee shop "
                         "to remove: ").strip().upper()

            # Call to function to return list index position and boolean value
            index, present = get_index_number(coffee_list, name)

            # Validating coffee shop name is in coffee_list
            if present is False:
                print('Invalid shop name. Please try again.')
                sys.exit()

            # Removing entry from coffee_list
            remove_val = coffee_list[index]
            coffee_list.remove(remove_val)

            # Calling function to write updates to file
            write_file(FILE, coffee_list)

            # Printing confirmation to console
            print('The entry {} has been removed.'.format(remove_val.get_name()))

        # Show coffee shops with all info
        elif user_input == 4:
            print('\n {0:15.0s} Displaying Coffee Inventory'.format(' '))
            # Printing __str__() method for class objects using for loop
            for x in range(len(coffee_list)):
                print('*', end=' ')
                print(coffee_list[x].__str__().upper())

        # Show top 5 coffee shops in inventory
        elif user_input == 5:

            # Print Header
            print('Top five coffee shops\n')

            # Appending class attributes rank and name to a sorted list
            for x in range(len(coffee_list)):
                sorted_coffee_list.append([coffee_list[x].get_rank(),
                                           coffee_list[x].get_name()])

            # Sorting list
            sorted_coffee_list = sorted(sorted_coffee_list)

            # Determining top five coffee shops depending on size of list
            if len(sorted_coffee_list) < 5:
                for x in range(len(sorted_coffee_list)):
                    print('Name:{0}, Rank:{1}'.
                          format(sorted_coffee_list[x][1],
                                 sorted_coffee_list[x][0]))
            else:
                for x in range(0, 5):
                    print('Name:{0}, Rank:{1}'.
                          format(sorted_coffee_list[x][1],
                                 sorted_coffee_list[x][0]))

        # Display Coffee Shop by name
        elif user_input == 6:

            name = input("Enter the name of the coffee shop "
                         "to display: ").strip().upper()

            # Call to function to return list index position and boolean value
            index, present = get_index_number(coffee_list, name)

            # Validating coffee shop name is in coffee_list
            if present is False:
                print('Invalid shop name. Please try again.')
                sys.exit()

            # Printing __str__() for class object if name is present in list
            else:
                print('{}'.format(coffee_list[index].__str__()))

        # Exit menu
        elif user_input == 0:
            print('You have selected to leave the menu.')
            sys.exit()

        # Validating menu choice
        else:
            print('You didn\'t enter a valid option.\n')
