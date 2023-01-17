import sys

def replace_punc_space(name):

	copy = ''
	for i in name:
		if (i == ',' or i == '!' or i == '?' or i == '.'):
			continue
		else:
			copy += i
	return (copy)

def create_new(my_list, n):

	new_list = []
	for items in my_list:
		if (len(items) > n):
			new_list.append(items)
	return (new_list)

def main(argv):
	try:
		if (len(argv) != 3 or argv[2].isdigit() == 0):
			raise Exception()
		else:
			new_str = replace_punc_space(argv[1])
			my_list = new_str.split()
			new_list = create_new(my_list, int(argv[2]))
			print(new_list)
	except:
		print("Error")

if __name__ == "__main__":
	main(sys.argv)
