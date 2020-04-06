# Program: animalGenerator.py
# This program creates and displays information about Animal objects.

import Animal


# Create a list for Animal objects
animals = []


# Print the menu for the available subclasses
def print_subclass_menu():
    print()
    print("Would you like to create a mammal or bird? ")
    print("1. Mammal")
    print("2. Bird")


# Returns the user's choice for the subclass
def get_subclass_choice():
    while True:
        try:
            choice = int(input("Which would you like to create? "))
            if choice < 1 or choice > 2:
                print(choice, "is not a valid choice.")
                continue
        except:
            print("Please enter a number between 1 and 2.")
        else:
            break

    return choice

# Gathers the user input for the mammal object
# and adds the object to the animal list
def build_mammal():
    # Ask the user for the animal's type and name
    animal_type = input("\nWhat type of mammal would you like to create? ")
    animal_name = input("What is the mammal's name? ")

    # Ask the user for the mammal's hair color
    hair_color = input("What color is the mammal's hair? ")

    # Create a new mammal object
    mammal = Animal.Mammal(animal_type, animal_name, hair_color)
    
    # Append the Animal object to the list
    animals.append(mammal)


# Gathers the user input for the bird object
# and adds the object to the animal list
def build_bird():
    # Ask the user for the animal's type and name
    animal_type = input("\nWhat type of bird would you like to create? ")
    animal_name = input("What is the bird's name? ")
    
    # Ask the user if the bird can fly
    can_fly = input("Can the bird fly? ")
    
    # Create a new bird object
    bird = Animal.Bird(animal_type, animal_name, can_fly)
    
    # Append the Animal object to the list
    animals.append(bird)


# Iterates through the animal list
# and prints information on each animal
def print_animal_list():
    # Print a header
    print("\nAnimal List")
    print("-----------")

    # Loop through the list
    for animal in animals:
        # Use accessor methods to get each Animal object's information
        animal_name = animal.get_name()
        animal_type = animal.get_animal_type()
        animal_mood = animal.check_mood()
    
        # Print the Animal object's information
        print(animal_name, "the", animal_type, "is", animal_mood)


# The main function that contains what the program is to do!
def main():
    # Print a welcome message
    print("Welcome to the animal generator!")
    print("This program creates Animal objects")

    while True:
        print_subclass_menu()
        
        choice = get_subclass_choice()
        
        if choice == 1:
            build_mammal()
        
        else:
            build_bird()
        
        # Ask the user if they would like to continue creating animals
        choice = input("\nWould you like to add more animals (y/n)? ")
        if choice != "y":
            break

    print_animal_list()


# Call the main() function to make the program do what it is defined to do.
main()
