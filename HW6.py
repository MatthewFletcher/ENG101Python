#HW 6 Python


hours_worked =float(input("How many hours did you work?>>> "))

wage_normal  = float(input("How much do you get paid in Dollars per hour>>> "))


wage_over = wage_normal * 1.5



if hours_worked <= 40:
	pay_regular  = hours_worked * wage_normal
	pay_over = 0


else:
	pay_regular = 40*wage_normal
	pay_over    = (hours_worked - 40) * wage_over

pay_total = pay_regular + pay_over

print("You will get paid $%.2f."%round(pay_total,2))
