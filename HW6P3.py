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
#  Program:  HW6P3                                                        #
# Due Date:  16 Nov 2017                                                  #
#                                                                         #
# Language:  Python 3.5.1                                                 #
#      IDE:  Python in Terminal                                           #
#                                                                         #
# Purpose:   Print table of Celsius and Farenheit temperatures            #
#   "Bugs":                                                               #
#   "Undocumented features": None.                                        #
###########################################################################





#Create list of Celcius points
cel = range(0,120,10)

#Print header
print(" C \t   F")

#use a for loop to create the table of points
for i in range(len(cel)-1):
	temp_c = cel[i]
	temp_f = temp_c*5/9+32
	print("%.2f\t %.2f"%(temp_c,temp_f)) 
