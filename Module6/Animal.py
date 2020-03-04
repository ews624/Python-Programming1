import random

class Animal:
    def __init__(self, __animal_type, __name, __mood):
        self.animal_type = __animal_type
        self.name = __name
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
        
        
    
        
    
