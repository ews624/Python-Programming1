from Animal import Animal
from Animal import Bird
from Animal import Mammal


program_run = True
zoo = []
print("Welcome to the animal generator!")
print("This program creates Animal objects.")
while(program_run):

    print("Would you like to create a mammal or bird?")
    print("1.Mammal")
    print("2.Bird")

    option = str(input("Which would you like to create?"))

    if(option == "1"):
        A_type = str(input("What type of animal would you like to create?"))
        A_name = str(input("What is the animal's name? "))
        A_mood = ""
        A_hair_color = str(input("What color is the mamal's hair?"))

        
        mammal = Mammal(A_type,A_name, A_hair_color)
        
        zoo.append(mammal)
    
        another_one= input('Would you like to add more animals? (y/n): ')
        if(another_one != 'y'):
            program_run = False
        
    if(option == "2"):
        A_type = str(input("What type of animal would you like to create?"))
        A_name = str(input("What is the animal's name? "))
        A_mood = ""
        A_can_fly = str(input("Can the bird fly?"))

        
        bird = Bird(A_type, A_name,  A_can_fly)

        zoo.append(bird)
    
        another_one= input('Would you like to add more animals? (y/n): ')
        if(another_one != 'y'):
            program_run = False

    else:
        print("")


print("Animal List")
for animal in zoo:
    print(animal.get_name() + " the " + animal.get_animal_type() + " is " + animal.check_mood())
   # print(A_name + " the " + A_type + " is " + Animal.check_mood )

