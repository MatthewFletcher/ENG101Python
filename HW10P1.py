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
#  Program:  HW10P1                                                       #
# Due Date:  15 Nov 2017                                                  #
#                                                                         #
# Language:  Python 3.5.1                                                 #
#      IDE:  Python in Terminal                                           #
#                                                                         #
# Purpose:   Print the intialism/acronym for a string of words            #
#   "Bugs":  Does not work for words that start with numbers              #
#   "Undocumented features": None.                                        #
###########################################################################


#HW 10


 #Cue for user input
print('Enter a series of words')
user_input = input(">>> ")

#Make user input all caps:
user_input = user_input.title()


#Create list for initials
initials = []

#Set a boolean "after_space" to true for first letter
#after_space = 1

#Iterate through words
for i in range(len(user_input)):
	if user_input[i].isupper():
		initials.append(user_input[i])

#Print result
#Create empty string for result of loop
result = ''

#Loop through each character in the list, and append it to the end
for i in range(len(initials)):
	result = result + initials[i]

#Print final result
print('The acronym for %s is %s'%(user_input,result))

