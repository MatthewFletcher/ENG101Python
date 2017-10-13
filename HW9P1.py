#    _     _      _     _      _     _      _     _      _     _      _     _
#   (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)
#    / ._. \      / ._. \      / ._. \      / ._. \      / ._. \      / ._. \
#  __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__
# (_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)
#    || O ||      || O ||      || O ||      || O ||      || O ||      || O ||
#  _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._
# (.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)
#  `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'

###########################################################################
#   Author:  Matt Fletcher                                                #
#    Class:  ENG101         	                                          #
#  Helpers:  None                                                         #
#                                                                         #
#  Program:  HW9P1                                                        #
# Due Date:  16 Nov 2017                                                  #
#                                                                         #
# Language:  Python 3.5.1                                                 #
#      IDE:  Python in Terminal                                           #
#                                                                         #
# Purpose:                                                                #
#   "Bugs":                                                               #
#   "Undocumented features": None.                                        #
###########################################################################


#Write a game of Rock Paper Scissor Lizard Spock

##############
#   Imports  #
##############
from random import randint

#Create a list of play options

t= ['ROCK','PAPER','SCISSOR','SPOCK','LIZARD']

#Set computer play to random choice 
computer =randint(0,len(t)-1)

print("The computer has chosen.")

#Get user choice
print('What would you like to play?')

#Because I'm lazy and don't want to type every option every time, plus makes it easier to debug
#Using a for loop to print list of choices
for i in range(len(t)):
	print('%i.\t%s'%((i+1),t[i]))
#Cue for user input
player_choice = int(input('Enter choice number here>>> ' ))

#Because list is indexed at 0, subtract 1 from the user's choice.
player = player_choice - 1

#Print out user's choice
print('You chose %s'%t[player])


#Now that user has input their choice, print computer's choice:
print('Computer chose %s'%t[computer])

#Figure out who actually won
#TODO make this cleaner

#I know this is absolutely ugly but I can't figure out a cleaner way to approach this 
#Set difference of player and computer to variable
determinant = player - computer
#If idx of player equals computer, declare tie
if player == computer:
    print("It's a tie!")
#If idx of player is 1 greater or 4 less than computer, player wins
if determinant == 1 or determinant == -4:
	print('Player wins')
#If idx of player is 2 greater or 3 less than computer,  computer wins:
if determinant == 2 or determinant == -3:
	print('Computer wins')
#If idx of player is 3 greater or 2 less than computer,  player wins
if determinant == 3 or determinant == -2:
	print('Player wins')
#If idx of player is 4 greater or 1 less than computer, computer wins
if determinant == 4 or determinant == -1:
	print('Computer wins')
