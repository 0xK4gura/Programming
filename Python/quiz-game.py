# Hola, welcome to my notes and practicals for creating a simple python projects
# coded directly and you may modify as you wish to get better with python.
# CTRL+F2 on highlighted word to edit multiple lines at once
# 
# Setting Up and asking if the user want to play the game
#
#

print("Welcome to my computer quiz")
name = input("What is your name? ") # setting up username to be return upon 

intro = "Hello {}! Do you want to play (Yes/No) \n" 
print(intro.format(name))
playing = input()

# playing = input("Hello ! Do you want to play? (Yes/No) \n").format(name) # \n means to break a new line

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) \n")
score = 0 # total number of score the user managed to get correct
qNo = 0 # total number of questions available. It increases as the template of the question below got replicated

# The quiz questions of the game

answer = input("What does CPU stand for? \n")
qNo += 1 # to increase the number of questions as to easily replicate later on
if answer.lower() == "central processing unit": # the 'lower' part means the variable is called and have every characters in lower case
    print("Correct! \n")
    score += 1 # same as score = score + 1
else:
    print("Incorrect!\n")    

answer = input("ًWhat does GPU stand for? \n")
qNo += 1
if answer.lower() == "graphics processing unit":
    print('Correct! \n')
    score += 1
else:
    print("Incorrect!\n")    

answer = input("What does RAM stand for? \n")
qNo += 1
if answer.lower() == "random access memory":
    print('Correct! \n')
    score += 1
else:
    print("Incorrect!\n")    

answer = input("What does PSU stand for? \n")
qNo += 1
if answer.lower() == "power supply":
    print('Correct! \n \n')
    score += 1
else:
    print("Incorrect!\n")    

# calculation and result output of the game

print("Your got " + str(score) + " questions correct!") # the integer must be converted into string to be printed out correctly
print("Your score is " + str((score/qNo)*100) + "%.") # the % of the questions that is correct 
