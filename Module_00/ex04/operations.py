import sys

def main(argv):
	try:
		counts = len(argv)
		if (counts == 3):
			a = int(argv[1])
			b = int(argv[2])
			print("Sum:       ", a + b)
			print("Difference:", a - b)
			print("Product:   ", a * b)
			if (b == 0):
				print("Quotient:  ERROR (division by zero)")
				print("Remainder: ERROR (module by zero)")
			else:
				print("Quotient:  ", a / b)
				print("Remainder: ", a % b)
		elif (counts > 3):
			print("AssertionError: too many arguments")
		elif (counts < 3):
			print('Usage: python operations.py <number1> <number2>')
			print('Example:\n', '   python operations.py 10 3')
	except:
			print("argument type is not digit")

if __name__ == "__main__":
	main(sys.argv)
