 #import random library to use random function
import random as rd

 #defining a list for the range of a dice
dice=[1,2,3,4,5,6] 

#user_defined function to return the random number
def Roll_dice():        
        no=rd.choice(dice)      #built_in random function in random library
        return(no)
        
#function that takes input as  Y,y or N,n    
def take_input():      
    print("Lets Play Roll The Dice!")
    print("Do you want to Roll the dice? Write 'Y' or 'N'")
    return input()

#function calling the Roll_dice()
def play():             

    print("\n")
    print(Roll_dice())
    print("\n")

#loop to keep the game continued       
while True:             
    ans=take_input()  
    if ans=='Y' or ans=='y':
        play()
    else:
        print("Do you want to play Again? Write 'Y' or 'N'")
        play_again=input()
        if play_again=='Y' or play_again=='y':
           play()
        else:
            break
