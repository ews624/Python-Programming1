import random


class Record:
    def __init__(self, name,wins,losses):
        self.__name = name
        self.__wins = wins
        self.__losses = losses

    def get_name(self):
        return self.__name

    def get_wins(self):
        return self.__wins

    def get_losses(self):
        return self.__losses

def print_Start_Menu():
    print("Welcome to Rock, Paper, Scissors!")
    print("")
    print("1.Start New Game")
    print("2.Load Game")
    print("3.Quit")

def print_RPS():
    print("1.Rock")
    print("2.Paper")
    print("3.Scissors")


def get_RPS_choice():
    while True:
        try:
            choice = int(input("\nWhat would you like to do?"))
            if choice < 1 or choice > 3:
                print(choice," is not a valid choice.")
                continue
        except:
            print("Please enter a number between 1 and 3.")
        else:
            break
        
    return choice

def check_for_RPS_file():
    fileName = "statistics.rps"
    try:
        f = open(fileName, "r+")

    except:
        f = open(fileName, "x+")
        return
    for record in f:
        token = record.split('+')
        stats = Record(token[0], int(token[1]), int(token[2]))
        timeline.append(stats)
    f.close()


def play_RPS():

    name = str(input("What is your name?"))
    wins = 0
    losses = 0
    for records in timeline:
        if name in records.get_name():
            wins = records.get_wins()
            losses = recoords.get_losses()
            
def create_RPS_Game():

    name = str(input("\nWhat is your name?"))
    newRecords = Record(name, 0,0)
    timeline.append(newRecords)
    RPS_Game_Play(name)

def New_RPS():
    check_for_RPS_file()
    create_RPS_Game()
    play_RPS()

def simulate_Game(choice):

    cpu_choice = random.randint(1, 3)

    if choice == cpu_choice:
        print("You and the computer both choose " choice " Tie")

    elif choice == 1 && cpu_choice == 2:
        print("You chose " choice ". The computer chose

   
        

def RPS_Game_Play(name):

    for record in timeline:
        if name in record.get_name():
           roundNumber = record.get_wins() + record.get_losses() + 1 

     
    print("Round ", roundNumber)
    print_RPS()
    choice = str(input("\nWhat will it be? ")
    
    
    
    
def main():
    print_Start_Menu()

    choice = get_RPS_choice()


    if choice == 1:
        New_RPS()

    if choice == 2:
        print()

    if choice == 3:
        print()

timeline = []
main()
