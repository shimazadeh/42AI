import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

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

def plot(x, y, theta):
	plt.scatter(x, y, color='blue')
	plt.plot(predict_(x, theta), color='red')
	plt.show()


def main():
	x = np.arange(1,6)
	y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])

	# Example 1:
	theta1 = np.array([[4.5],[-0.2]])
	plot(x, y, theta1)

	# Example 2:
	theta2 = np.array([[-1.5],[2]])
	plot(x, y, theta2)

	# Example 3:
	theta3 = np.array([[3],[0.3]])
	plot(x, y, theta3)


if __name__ == "__main__":
	main()
