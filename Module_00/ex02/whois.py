import sys

def	main(argv):

	if (len(argv) == 2):
		try:
			num = int(argv[1])
			if (num == 0):
				print("I'm Zero.")
			elif (num % 2):
				print("I'm Odd.")
			else:
				print("I'm Even.")
		except:
			print("AssertionError: argument is not an int!")
	elif (len(argv) > 2):
		print("AssertionError: more than one argument are provided")

if __name__ == "__main__":
	main(sys.argv)
