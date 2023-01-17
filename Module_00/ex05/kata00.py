# Put this at the top of your kata00.py file
kata = (19,42,21)

import sys

def main(argv):
	thistuple = (kata[0], kata[1], kata[2])

	print("the three numbers are:", end =" ")
	for i in thistuple:
		print(i, end= ", ")



if __name__ == "__main__":
	main(sys.argv)
