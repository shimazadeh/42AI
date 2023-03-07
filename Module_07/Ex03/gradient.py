import numpy as np
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

def gradient(x, y, theta):
	"""Computes a gradient vector from three non-empty numpy.array, without any for-loop.
	The three arrays must have the compatible dimensions.
	Args:
	x: has to be an numpy.array, a matrix of dimension m * n.
	y: has to be an numpy.array, a vector of dimension m * 1.
	theta: has to be an numpy.array, a vector (n +1) * 1.
	Return:
	The gradient as a numpy.array, a vector of dimensions n * 1,
	containg the result of the formula for all j.
	None if x, y, or theta are empty numpy.array.
	None if x, y and theta do not have compatible dimensions.
	None if x, y or theta is not of expected type.
	Raises:
	This function should not raise any Exception.
	"""
	if x is None or y is None or theta is None:
		return 0
	if len(x) != len(y):
		return 0
	x_new = add_intercept(x)
	x_t = np.transpose(x_new)
	m = len(x_new)
	delta_J = (np.dot(x, theta) - y) / m # this should be x_new not x to match the method in module06
	delta_J = np.dot(x_t, delta_J)
	return (delta_J)

def main():
	x = np.array([
	[ -6, -7, -9],
	[ 13, -2, 14],
	[ -7, 14, -1],
	[ -8, -4, 6],
	[ -5, -9, 6],
	[ 1, -5, 11],
	[ 9, -11, 8]])
	y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((-1, 1))
	theta1 = np.array([3,0.5,-6]).reshape((-1, 1))
	# Example :
	print(gradient(x, y, theta1))
	# Output:
	# array([[ -33.71428571], [ -37.35714286], [183.14285714], [-393.]])

	# Example :
	theta2 = np.array([0,0,0]).reshape((-1, 1))
	print(gradient(x, y, theta2))
	# Output:
	# array([[ -0.71428571], [ 0.85714286], [23.28571429], [-26.42857143]])

if __name__ == "__main__":
	main()
