import random 


def display_title():
	print('Let\'s play guess the number!')

def play_game():
	low = 1
	high = 10
	number = random.randint(low,high)
	print('Guess a number between %i and %i'%(low,high))
	count = 1
	
	solved = 0
	while solved == 0:
		guess = int(input('Your guess, please>> '))
		if guess < number:
			print('Too low')
			count += 1
		elif guess > number:
			print('Too high')
			count += 1
		else:
			print('Success in %i tries!!'%count)
			solved = 1
def main():
	display_title()
	again = 'y'
	while again.lower() == 'y':
		play_game()
		print()
		again = input('Play game again? y/n >>> ')
	print('Bye!')


if __name__ == '__main__':
	main()
