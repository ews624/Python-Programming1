import random

class Animal:
    def __init__(self, __animal_type, name):
        self.animal_type = __animal_type
        self.name = name
        choice = random.randrange(2) + 1
        if(choice == 1):
            self.mood = "happy"
        if(choice == 2):
            self.mood = "hungry"
        if(choice == 3):
            self.mood = "sleepy"
          
    def get_name(self):
        return self.name

    def get_animal_type(self):
        return self.animal_type

    def check_mood(self):
        return self.mood

    
class Mammal(Animal):
    def __init__(self,name, mammal_type, hair_color):
        self.__hair_color = hair_color
        Animal.__init__(self, name, mammal_type)

    def get_hair_color(self):
        return self.hair_color

class Bird(Animal):
    def __init__(self, birdtype,name, can_fly):
        self.can_fly = can_fly
        Animal.__init__(self,birdtype,name)

    def get_can_fly(self):
        return self.can_fly

    
        
    
        
    
