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
#  Program:  HW8P3                                                        #
# Due Date:  16 Nov 2017                                                  #
#                                                                         #
# Language:  Python 3.5.1                                                 #
#      IDE:  Python in Terminal                                           #
#                                                                         #
# Purpose:                                                                #
#   "Bugs":                                                               #
#   "Undocumented features": None.                                        #
###########################################################################
###########
# Imports #
###########
import math




#Set acceleration due to gravity
g = 9.8

#Create list of velocity points
v = [10,12,14,16,18,20]

#Create list of angles
theta = [50,60,70,80,90]

#Create list for height results for each angle
height = []

#Create list for max heights
height_max = []

#Define height function
def get_height(vel,ang):
	height = vel**2 * math.sin(ang)/(2*g)
	return round(height,2)


##########################################
#Print result as a table

def newLine():
	print('\n')

#Printing top row
#Print cell 0,0
print('V\Theta', end = '\t')

#Print rest of first row (angle values)
for i in theta:
	print(i,end = '\t')


##########################################
#Printing rest of rows#
#Loop through rest of rows

#Define printing of rows
def rowPrint():
	print('\n')
	#Print  data in row
	print(v[row],end = '\t')
	for ang in theta: 
		print(get_height(v[row],ang), end = '\t')

#Execute function

#Loop through rest of rows
for row in range(len(v)-1):
	row = row + 1
	rowPrint()

#Print new line for my sanity
newLine()
