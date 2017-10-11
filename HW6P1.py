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
#  Program:  HW6P1                                                        #
# Due Date:  16 Nov 2017                                                  #
#                                                                         #
# Language:  Python 3.5.1                                                 #
#      IDE:  Python in Terminal                                           #
#                                                                         #
# Purpose:                                                                #
#   "Bugs":                                                               #
#   "Undocumented features": None.                                        #
###########################################################################


#HW 6 Python

#Input number of hours worked
hours_worked =float(input("How many hours did you work?>>> "))


#Cue user for hourly wage
wage_normal  = float(input("How much do you get paid in Dollars per hour>>> "))

#Set wage_over to pay and a half
wage_over = wage_normal * 1.5


#Check if the person worked more than 40 hours in a week. 
if hours_worked <= 40:
	#Calculate regular pay
	pay_regular  = hours_worked * wage_normal
	#This step is necessary to allow the ending print statement to work. 
	pay_over = 0


else:
	#Calculate regular pay for first 40 hours
	pay_regular = 40*wage_normal
	#Calcalate overtime pay
	pay_over    = (hours_worked - 40) * wage_over


#Calculate total pay
pay_total = pay_regular + pay_over


#Print final result
print("You will get paid $%.2f."%round(pay_total,2))
