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
#  Program:  HW8P2                                                        #
# Due Date:  16 Nov 2017                                                  #
#                                                                         #
# Language:  Python 3.5.1                                                 #
#      IDE:  Python in Terminal                                           #
#                                                                         #
# Purpose:   Find value of Leibnitz equation for given values             #
#   "Bugs":                                                               #
#   "Undocumented features": None.                                        #
###########################################################################

############
# Imports  #
############
import math
import time
'''
#HW8P2

#Create list with desired numbers of iterations
iteration_num = [1000,10000,100000,1000000]

#Create empty list for sums
sum_list = []

#For loop through each value of iteration_num
for i in range(len(iteration_num)):
	#Initialize iteration count to 0 for each run through loop
	k = 0
	sum_total = 0
	sum = 0

	
	#Calculate leibnitz sum
	while k < iteration_num[i]:
		sum = ((-1)**k)/(2*k + 1)
		sum_total = sum+sum_total
		k = k+1
		
	#Append final sum value for each iteration_num to list
	sum_list.append(sum_total)


#Print header
print('Desired value: %f'%(math.pi/4))
print('Count\tValue')
for i in range(len(iteration_num)):
	print('%i\t%f'%(iteration_num[i],sum_list[i]))

'''


######
#Part 2, finding required number of iterations to be within 10^-6 of required  value

#Clear sum value
sum = 0

#Set iteration count to zero
iteration_count = 0

#Desired value
desired_value = math.pi/4

#Current value
current_value = 0

#Acceptable error
error_ok = 10**(-6)

#While loop
while math.fabs(current_value - desired_value) > error_ok:
	#Delay a half second between iterations for debugging

	#TODO remove this for final product
	#time.sleep(0.5)
	sum = (-1)**iteration_count/(2*iteration_count+1)+sum


	#Set current value equal to the sum
	current_value = sum

	iteration_count = iteration_count + 1
	#Print for debugging
	#print(iteration_count,current_value)

#Print final result 
print('It takes %i iterations to get within the desired value of pi/4.'%(iteration_count))
