def to_celsius(fahrenheit):
	celsius = (fahrenheit -32)*5/9
	return celsius

def to_fahrenheit(celsius):
	fahrenheit = celsius * 9/5 + 32
	return fahrenheit

def main():
	for temp in range(0,212,40):
		print(temp, "F =", round(to_celsius(temp)), "C")
	
	for temp in range(0,100,20):
		print(temp, "C =", round(to_fahrenheit(temp)), "F")
		
if __name__ == "__main__":
    main()
