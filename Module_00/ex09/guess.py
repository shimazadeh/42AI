import sys
import random

def main(argv):
	print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType /'/exit' to end the game.\nGood luck!\n")
	i = 0

	number = 3
	while True:
		data = input("What's your guess between 1 and 99?\n")
		if 'exit' == data:
			print("Goodbye!")
			return
		elif (data.isdigit() == 0):
			print("that's not a number")
		elif data < str(number):
			print("too low")
		elif data > str(number):
			print("too high")
		elif (data == str(number) and number == 42):
			print("The answer to the ultimate question of life, the universe and everything is 42.")
		if (data == str(number) and i == 0):
			print("Congratulations, you got it on the first try!")
			return
		elif data == str(number):
			print("Congratulations, you've got it!")
			return
		i += 1


if __name__ == "__main__":
	main(sys.argv)
