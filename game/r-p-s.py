import random
# welcome to my rock-paper-scissors game, have fun playing and scruntinizing the code!!!
#we are going over some basic rules in the game and we will prompt the user to enter a choice.
rules = "Welcome to the rock, paper, scissors game.\n Note the rules....\n \"R\" is for rock\n \"P\" is for paper""\n \"S\" is for scissors\n Rock beats scissors, scissors beats paper and paper beats rock.\n Happy playing!!!"
print(rules)

options = ["R", "P", "S"]

def playagain():
    print("\n\n Would you like to play again")
    ans = input("Enter \"y\" for yes or \"n\" for no ")
    if ans == "y":
       validate()
    else:
        print("\n\nThank you for playing, byebye!!")
        
def validate():
    userchoice = input("\n \n Enter your choice: \n R, P or S: ")
    corrected = userchoice.upper()
#Now i want to make sure the user enters the right input.
    while corrected not in options:
          print("Not a choice!!!")
          validate()
          break
         #let's have my motherboard make a choice. Rooting for my cpu!!!
    cpuchoice = random.choice(options)
    print("Cpu chooses: " + cpuchoice)
    #Now let's decide the winner *smirks* and i do hope it's not a tie
    while corrected == cpuchoice:
       print("oh!.., its a tie.")
       playagain()
       break
    if corrected == "R":
         if cpuchoice == "S":
           print("You winnn!!!\nMy cpu sucks at playing games")
           playagain()
    elif corrected == "S":
         if cpuchoice == "R":
            print("Cpu winnsss!!! Better luck next time..")
            playagain()
    elif corrected == "P": 
         if cpuchoice == "R":
            print("You winnn!!!\nMy cpu sucks at playing games")
            playagain()
    elif corrected == "R": 
         if cpuchoice == "P":
             print("Cpu winnsss!!! Better luck next time..")
             playagain()
    elif corrected == "S": 
         if cpuchoice == "P":
            print("You winnn!!!\nMy cpu sucks at playing games")
            playagain()
    elif corrected == "p": 
         if cpuchoice == "S":
            print("Cpu winnsss!!! Better luck next time..")
            playagain()   
validate()