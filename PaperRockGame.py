# Steps
#List of options => S , P , R
#user select an option
#pc select an option
#compare selections => show winner of the round
#repeat till 3 rounds and show winner of most rounds won.
import random as rnd
user_score=0
pc_score=0
run =True

 #step 1 
options =["s","r","p"]

while run:
    #step 2
    user_select=input("please enter an option\n")
    # step 3
    pc_select = rnd.choice(options)
    print(f"pc choice is : {pc_select}")
    #step 4
    if user_select == pc_select:
        print("draw , lets go for another choice")
    elif user_select =="s":
        if pc_select=="p":
           pc_score+=1
        else:
            user_score+=1
    elif user_select=="p":
        if pc_select=="s":
           pc_score+=1
        else:
            user_score+=1
    elif user_select=="r":
        if pc_select=="p":
            pc_score+=1
        else:
            user_score+=1    
    # Exit Conditon for run:False
    if user_score ==3 or pc_score == 3:
        if user_score==3:
            print("user won the game!")
        else:
            print("pc won the game")
        run =False
    else:
        print(f"user score: {user_score} and pc score: {pc_score}\nLets go for another Round")    