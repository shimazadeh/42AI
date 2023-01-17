# Put this at the top of your kata02.py file

kata = (2019, 9, 25, 3, 30)

import sys

def	swap(tup):
	mylist = list(tup)
	tmp = mylist[0]

	mylist[0] = mylist[1]
	mylist[1] = mylist[2]
	mylist[2] = tmp
	return (mylist)

def convertTuple(tup):
	name = ''
	i = 0

	my_list = swap(tup)
	while (i < len(my_list)):
		if (my_list[i] < 0):
			raise Exception()
		if (i != 2 and len(str(my_list[i])) != 2):
			name = name + '0' + str(my_list[i])
		else:
			name = name + str(my_list[i])
		i += 1
	return name

def print_format(str):

	i = 0
	while(i < len(str)):
		if (i < 5 and i > 0 and i % 2 == 0):
			print("/" , end="")
		if (i == 8):
			print(" ", end="")
		if (i == 10):
			print(":", end="")
		print(str[i], end="")
		i += 1


def main(argv):
	try:
		str = convertTuple(kata)
		print_format(str)
	except Exception:
		print("Tuple include negative number")

if __name__ == "__main__":
	main(sys.argv)
