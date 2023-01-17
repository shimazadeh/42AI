import sys

def convert(string):
	MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
						'C':'-.-.', 'D':'-..', 'E':'.',
						'F':'..-.', 'G':'--.', 'H':'....',
						'I':'..', 'J':'.---', 'K':'-.-',
						'L':'.-..', 'M':'--', 'N':'-.',
						'O':'---', 'P':'.--.', 'Q':'--.-',
						'R':'.-.', 'S':'...', 'T':'-',
						'U':'..-', 'V':'...-', 'W':'.--',
						'X':'-..-', 'Y':'-.--', 'Z':'--..',
						'a':'.-', 'b':'-...',
						'c':'-.-.', 'd':'-..', 'e':'.',
						'f':'..-.', 'g':'--.', 'h':'....',
						'i':'..', 'j':'.---', 'k':'-.-',
						'l':'.-..', 'm':'--', 'n':'-.',
						'o':'---', 'p':'.--.', 'q':'--.-',
						'r':'.-.', 's':'...', 't':'-',
						'u':'..-', 'v':'...-', 'w':'.--',
						'x':'-..-', 'y':'-.--', 'z':'--..',
						'1':'.----', '2':'..---', '3':'...--',
						'4':'....-', '5':'.....', '6':'-....',
						'7':'--...', '8':'---..', '9':'----.',
						'0':'-----'}
	new_string = ''
	for letter in string:
		if (letter != ' '):
			new_string += MORSE_CODE_DICT[letter] + ' '
		elif (letter == ' '):
			new_string += '/ '
		else:
			raise Exception()
	return (new_string)

def combine(argv):
	new_string = ''
	i = 1
	while (i < len(argv)):
		if (i == len(argv) - 1):
			new_string += argv[i]
		else:
			new_string += argv[i] + ' '
		i += 1
	return new_string

def main(argv):

	try:
		if (len(argv) > 1):
			if (len(argv) > 2):
				string = combine(argv)
			else:
				string = argv[1]
			new_string = convert(string)
			print(new_string)
	except:
		print("Error")

if __name__ == "__main__":
	main(sys.argv)
