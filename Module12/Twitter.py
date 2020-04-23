from Tweet import Tweet 
import time

def check_for_Tweet_file():
    fileName = "tweets.dat"
    try:
        f = open(fileName, "r+")

    except:
        f = open(fileName, "x+")
        return
    for tweet in f:
        token = tweet.split('+')
        oldtweets = Tweet(token[0], token[2], float(token[1]))
        timeline.append(oldtweets)
    f.close()
    
def print_Menu():
    print("Tweet Menu")
    print("-----")
    print("1.Make a Tweet")
    print("2.View Recent Tweets")
    print("3.Search Tweets")
    print("4.Quit")


def get_Tweet_choice():
    while True:
        try:
            choice = int(input("\nWhat would you like to do?"))
            if choice < 1 or choice > 4:
                print(choice," is not a valid choice.")
                continue
        except:
            print("Please enter a number between 1 and 4.")
        else:
            break
        
    return choice

def make_Tweet():
    name = str(input("\nWhat is your name?"))
    text = str(input("What would you like to tweet?"))

    while(len(text) >140):
        print("Tweets can only be 140 characters!")
        text = input("What would you like to tweet?")

    newTweet = Tweet(name, text, 0)
    timeline.append(newTweet)

def view_Tweet():
    print("Recent Tweets")
    print("----")

    if len(timeline) == 0:
        print("There are no recent tweets.")

    else:
        for tweet in timeline:
            age = time.time() - tweet.get_age()
            if (age) < 60:
                age = str(int(age)) + 's'
            elif 60 < (age) < 3600:
                age = str(int(age/60)) + 'm'
            elif 3600 < (age):
                age = str(int(age/3600)) + 'h'
            print(tweet.get_author() + "-" + age)
            print(tweet.get_text())

def search_Tweets():

    if len(timeline) == 0:
        print("There are no tweets to search")
        return
    
    searchToken = input("What would you like to search for?")
    results = 0
    while searchToken == 0:
        searchToken = input("What would you like to search for?")

    print("Search Results")
    print("-----")

    for tweet in timeline:
        if searchToken in tweet.get_text():
            age = time.time() - tweet.get_age()
            if (age) < 60:
                age = str(int(age)) + 's'
            elif 60 < (age) < 3600:
                age = str(int(age/60)) + 'm'
            elif 3600 < (age):
                age = str(int(age/3600)) + 'h'
            print(tweet.get_author() + "-" + age)
            print(tweet.get_text())
            results += 1
    if results == 0:
        print("No tweets contained ", searchToken)
    print("")
def exit_Twitter():

    fileName = "tweets.dat"
    try:
        file = open(fileName, "r+")

    except:
        print("Print couldn't open file")
        exit()    
    for tweet in timeline:
        file.write(tweet.get_author() + '+' + str(tweet.get_age()) + '+' + tweet.get_text() + '+\n')

    file.close()
    print("Thank you for using the Tweet Manager!")
    


def main():
    while(True):
        check_for_Tweet_file()
        print_Menu()

        choice = get_Tweet_choice()

        if choice == 1:
            make_Tweet()

        if choice == 2:
            view_Tweet()
        
        if choice == 3:
            search_Tweets()
        
        if choice == 4:
            exit_Twitter() 
            break


timeline = []

main()
