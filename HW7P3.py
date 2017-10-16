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
#  Program:  HW7P3                                                        #
# Due Date:  1 Nov 2017                                                   #
#                                                                         #
# Language:  Python 3.5.1                                                 #
#      IDE:  Python in Terminal                                           #
#                                                                         #
# Purpose:                                                                #
#   "Bugs": Cube sum off by 1 cube                                        #
#   "Undocumented features": None.                                        #
###########################################################################

#########
#Imports#
#########

#Create function to return sum of first n natural numbers
def sumN(n):
	#Initialize sum
	sum = 0
	for i in (range(1,n)):
		sum = sum + i
	print("The sum of the first %i numbers is %i"%(n,sum))


#Create function to return sum of cubes of first n natural numbers
def sumNcubes(n):
	#Initialize sum_cubes
	sum_cubes = 0
	#Use for loop to add the numbers
	for i in (range(1,n+1)):
		sum_cubes = sum_cubes + (i)**3
	print("The sum of the first %i cubes is %i"%(n,sum_cubes))


#Cue input for desired number to check
n = int(input("Enter a number here >>> "))



#Call functions with input from user input above
sumN(n)
sumNcubes(n)

