from Animal import Animal

program_run = True
zoo = []
print("Welcome to the animal generator!")
print("This program creates Animal objects.")
while(program_run):
    
    A_type = str(input("What type of animal would you like to create?"))
    A_name = str(input("What is the animal's name? "))
    A_mood = "" 
    
    animal = Animal(A_type, A_name, A_mood)

    zoo.append(animal)
    
    another_one= input('Would you like to add more animals? (y/n): ')
    if(another_one != 'y'):
            program_run = False

print("Animal List")
for obj in zoo:
    print(animal.get_name() + " the " + animal.get_animal_type() + " is " + animal.check_mood())
   # print(A_name + " the " + A_type + " is " + Animal.check_mood )

