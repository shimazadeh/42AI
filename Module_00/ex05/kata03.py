# Put this at the top of your kata02.py file

kata = "The right format"

import sys

def main(argv):
	if (len(kata) > 42):
		raise Exception("invalid length")
	else:
		i = 0
		while (i < 41 - len(kata)):
			print("-", end="")
			i += 1
		print(kata, end="")

if __name__ == "__main__":
	main(sys.argv)
