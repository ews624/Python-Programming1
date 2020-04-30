import random

gameDictionary = dict({1: "Rock", 2:"Paper", 3:"Scissors"})
resultDictionary = dict({1: "win", -1: "lose", 0: "tie"})


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

def print_Menu2():
    print("\n1. Play again")
    print("2. View Statistics")
    print("3. Quit")

def get_RPS_choice():
    while True:
        try:
            choice = int(input("\nEnter choice: "))
            if choice < 1 or choice > 3:
                print(choice," is not a valid choice.")
                continue
        except:
            print("Please enter a number between 1 and 3.")
        else:
            break
        
    return choice

def check_for_RPS_file(name):
    fileName = name + ".rps"
    try:
        f = open(fileName, "r+")
    except:
        f = open(fileName, "x+")
        f.close()
        return
    f.close()


def load_RPS():
    name = str(input("\nWhat is your name?"))
    fileName = name+".rps"
    try:
        with open(fileName) as f:
            stats = f.readlines()
        ##finish later

        print("Welcome back ", name,". Let's Play!")
    except:
        print(name, ", your game could not be found")
    
    
def simulate_Game(choice,cpu_choice):

    if (choice == 1) & (cpu_choice == 1):
        return 0
    elif (choice == 1) & (cpu_choice == 2):
        return -1
    elif (choice == 1) & (cpu_choice == 3):
        return 1
    elif (choice == 2) & (cpu_choice == 1):
        return 1
    elif (choice == 2) & (cpu_choice == 2):
        return 0
    elif (choice == 2) & (cpu_choice == 3):
        return -1
    elif (choice == 3) & (cpu_choice == 1):
        return -1
    elif (choice == 3) & (cpu_choice == 2):
        return 1
    elif (choice == 3) & (cpu_choice == 3):
        return 0
    
def RPS_Game_Play():

    print("Round ", stats[4])
    print_RPS()
    choice = int(input("\nWhat will it be? "))
    while choice < 1 or choice > 3:
        print_RPS()
        choice = int(input("\nWhat will it be? "))

    cpu_choice = random.randint(1, 3)
    
    RPS_Result = simulate_Game(choice, cpu_choice)

    print("You chose " + gameDictionary[choice] + ". The computer chose " +
          gameDictionary[cpu_choice] + ". You " + resultDictionary[RPS_Result])       

    return RPS_Result

def save_file():
    try:
        file = stats[0] + ".rps"
        save_file = open(file, "w")
        save_file.write(stats[0])
        save_file.write("\n"+stats[1])
        save_file.write("\n",stats[2])
        print(stats[0] + ", your game has been saved.")
    except:
        print("Save Failed")

def New_RPS():
    
    
    name = str(input("\nWhat is your name?"))
    check_for_RPS_file(name)
    print("Hello", name,". Let's Play!")
    stats.append(name)
    stats.append(0)
    stats.append(0)
    stats.append(0) 
    stats.append(1)

    result = RPS_Game_Play()
    
    if (result == -1):
        stats[2] = stats[2] + 1
    elif (result == 0):
        stats[3] = stats[3] + 1
    elif (result == 1):
        stats[1] = stats[1] + 1
    stats[4] = stats[4] + 1
    
    
def main():
    print_Start_Menu()

    choice = get_RPS_choice()

    if choice == 1:
        New_RPS()

    if choice == 2:
        load_RPS()

    if choice == 3:
        return

    while 1:
        
        print("\nWhat would you like to do? ")
        print_Menu2()

        choice2 = get_RPS_choice()
        
        if choice2 == 1:

            result = RPS_Game_Play()
            if (result == -1):
                stats[2] = stats[2] + 1
            elif (result == 0):
                stats[3] = stats[3] + 1
            elif (result == 1):
                stats[1] = stats[1] + 1
            stats[4] = stats[4] + 1

        elif choice2 == 2:
            print(stats[0] + ", here are your gameplay statistics...")
            print("Wins:",stats[1])
            print("Losses:",stats[2])
            print("Ties:",stats[3])
            try:
                print("Win/Loss Ratio:",(float(stat[1])/float(stats[2])))
            except:
                print("Win/Loss Ratio:",0.0)

        elif choice2 == 3:
            save_file()
            break

stats = []
main()
