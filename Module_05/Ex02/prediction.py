import numpy as np
import math
import pandas as pd

def add_intercept(x):
	if x is None:
		return 0
	df = pd.DataFrame(x)
	num_columns = len(df.axes[1])
	first_column = df.pop(0)
	df.insert(0, 0, 1)

	i = 1
	while(i < num_columns + 1):
		if (i < num_columns):
			next_column = df.pop(i)
		else:
			next_column = 0
		df.insert(i, i, first_column)
		first_column = next_column
		i = i + 1
	x = df.to_numpy()
	return (x)

def predict_(x, theta):
	if x is None or theta is None:
		return 0
	z = add_intercept(x)
	if (len(pd.DataFrame(z).axes[1]) != len(theta)):
		return 0
	return (np.dot(z, theta))

def main():
	x = np.arange(1,6)

	theta1 = np.array([[5], [0]])
	print("Example2: \n", predict_(x, theta1))

	theta2 = np.array([[0], [1]])
	print("Example2: \n", predict_(x, theta2))

	theta3 = np.array([[5], [3]])
	print("Example3: \n", predict_(x, theta3))

	theta4 = np.array([[-3], [1]])
	print("Example4: \n", predict_(x, theta4))


if __name__ == "__main__":
	main()
