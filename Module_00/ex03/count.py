
import sys
import string

def	text_analyzer(arg):

	try:
		result = str(arg)
		uppercase_count = 0
		lowercase_count = 0
		pun_count = 0
		space_count = 0

		for char in result:
			if (char.isupper()):
				uppercase_count += 1
			elif (char.islower()):
				lowercase_count += 1
			elif (char.isspace()):
				space_count += 1
			elif (char in string.punctuation):
				pun_count += 1
		print("the text contain", len(arg), "character(s):")
		print("-", uppercase_count, "upper letter(s)")
		print("-", lowercase_count, "lower letter(s)")
		print("-", pun_count, "punctuation mark(s)")
		print("-", space_count, "space")
	except:
		print("AssertionError: the argument is not a string")

def	main(argv):
	text_analyzer(argv[1])

if __name__ == "__main__":
	main(sys.argv)


