
#
import random


#
playerDie1 = random.randint(1,6)
playerDie2 = random.randint(1,6)
playerDie3 = random.randint(1,6)
playerDice = [playerDie1, playerDie2, playerDie3]

#
print(playerDice)
playerTotal = 0

#
for x in playerDice:
    playerTotal=playerTotal+x
print("Player's total: "+ str(playerTotal))

#
computerDie1 = random.randint(1,6)
computerDie2 = random.randint(1,6)
computerDie3 = random.randint(1,6)
computerDice = [computerDie1, computerDie2, computerDie3]

print(computerDice)
computerTotal = 0

for y in computerDice:
    computerTotal=computerTotal+y
print("computer's total: "+ str(computerTotal))


#
if playerTotal > 12:
    print("Busted. You lose")

#    
else:
    answer = input("Would you like to keep playing? (Y/N)")
#
    if answer == "Y":
        play1 = input("Which die would you like to throw again?")

#        
        if play1 == "1":
            die1 = random.randint(1,6)
            playerDice[0]=die1
                
        elif play1 == "2":
            die2 = random.randint(1,6)
            playerDice[1]=die2
        else:
            die3 = random.randint(1,6)
            playerDice[2]=die3
#        
    playerTotal = 0
    for x in playerDice:
        playerTotal=playerTotal+x

#     
if playerTotal > 12:
    print(playerDice)    
    print("Player's total: "+ str(playerTotal))
    print("Busted. You lose")

elif computerTotal > 12:
    print(playerDice)    
    print("Player's total: "+ str(playerTotal))
    print("Computer's total: "+ str(computerTotal))
    print("Computer busted. You win!")
    
elif playerTotal == 12:
    print(playerDice)    
    print("Player's total: "+ str(playerTotal))
    print("Computer's total: "+ str(computerTotal))
    print("You win!")
    
elif computerTotal < 12 and playerTotal > computerTotal:
    print(playerDice)    
    print("Player's total: "+ str(playerTotal))
    print("Computer's total: "+ str(computerTotal))
    print("You win!")
    
else:
    print(playerDice)    
    print("Player's total: "+ str(playerTotal))
    print("Computer's total: "+ str(computerTotal))
    print("You lose!")

