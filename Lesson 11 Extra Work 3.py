import random
num = random.randint(10,20)
while True:
    userchoice = int(input("Please guess a number between 10 and 20: "))
    if userchoice == num:
       print ("You guessed the number!")
       break 