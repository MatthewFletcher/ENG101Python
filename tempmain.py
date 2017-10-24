import temperature as temp

def display_menu():
	print('MENU')
	print('1. F to C')
	print('2. C to F')



def main():
	display_menu()
	again = 'y'
	while again.lower()=='y':
		convert_temp()
		print()
		again = input('Try again? y/n>>> ')
		print()
	print('Bye')



def convert_temp():
	option = int(input('Enter a menu optino:'))
	if option == 1:
		f = int(input('Enter degrees F:'))
		c = temp.to_celsius(f)
		c = round(c,2)
		print('Degree Celsius: %f'%c)
	elif option == 2:
		c = int(input('Enter degrees C:'))
		f = temp.to_degrees(c)
		f = round(f,2)
		print('Degree Farenheit: %f'%f)
	else:
		print('Enter a valid number')

if __name__ == '__main__':
	main()
