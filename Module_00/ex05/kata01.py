# Put this at the top of your kata01.py file
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

import sys

def main(argv):
	filler = "was created by"
	keys = kata.keys()

	for i in keys:
		print(i, filler, kata[i])

if __name__ == "__main__":
	main(sys.argv)
