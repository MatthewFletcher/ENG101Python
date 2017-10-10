#HW 6 Python


hours_worked =float(input("How many hours did you work?>>> "))

wage_normal  = float(input("How much do you get paid in Dollars per hour>>> "))


wage_over = wage_normal * 1.5



if hours_worked <= 40:
	pay = hours_worked * wage_normal
else:
	
