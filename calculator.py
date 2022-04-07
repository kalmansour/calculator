
def main():
	while True:
		try:
			first_number = int(input("Enter the first number:"))
			second_number = int(input("Enter the second number:"))
			operation = input("Choose the operation (+, -, /, *):")
			calculator = eval(f'{first_number}{operation}{second_number}')

			while operation not in ['+', '-', '/','*']:
				break
			else:
				print(f'The answer is {calculator}')
			break
		except (ValueError): 
			print("Oops!  That was not a valid number.  Try again...")
		except (SyntaxError): 
			print("Oops!  That was not a valid operation.  Try again...")
		
	pass
	



if __name__ == '__main__':
	main()
