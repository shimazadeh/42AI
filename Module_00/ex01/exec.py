#!/usr/bin/python

import sys

def	main(argv):

	for i in reversed(range(1, len(argv))):
		for j in reversed(range(0, len(argv[i]))):
			if (argv[i][j].isupper()):
				print(argv[i][j].lower(), end='')
			else:
				print(argv[i][j].upper(), end='')
		if i > 1:
			print(" ", end='')
		else:
			print()


if __name__ == "__main__":
	main(sys.argv)
