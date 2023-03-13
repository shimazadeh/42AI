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

def sigmoid_(x):
	sig_ = np.zeros((len(x), 1))
	for i in range(len(x)):
		sig_[i] = 1 / ( 1 + math.e ** -(x[i]))
	return (sig_)

def logistic_predict_(x, theta):
	x_ = add_intercept(x)
	res = np.dot(x_, theta)
	sig_ = sigmoid_(res)
	return (sig_)

def log_gradient(x, y, theta):
	"""Computes a gradient vector from three non-empty numpy.ndarray, with a for-loop. The three arrays must have compatiblArgs:
	x: has to be an numpy.ndarray, a matrix of shape m * n.
	y: has to be an numpy.ndarray, a vector of shape m * 1.
	theta: has to be an numpy.ndarray, a vector of shape (n + 1) * 1.
	Returns:
	The gradient as a numpy.ndarray, a vector of shape n * 1, containing the result of the formula for all j.
	None if x, y, or theta are empty numpy.ndarray.
	None if x, y and theta do not have compatible dimensions.
	Raises:
	This function should not raise any Exception.
	"""
	x_ = add_intercept(x)
	h_ = logistic_predict_(x, theta)
	J_ = np.zeros((len(x[0] + 1), 1), dtype=float)
	m = len(x)

	for i in range(m):
		J_[0] = J_[0] + (h_[i] - y[i]) / len(x)
		J_[1] = J_[1] + (h_[i] - y[i]) * x_[i] / len(x)
	return (J_)

def main():
	# Example 1:
	# y1 = np.array([1]).reshape((-1, 1))
	# x1 = np.array([4]).reshape((-1, 1))
	# theta1 = np.array([[2], [0.5]])
	# print(log_gradient(x1, y1, theta1))
	# Output:
	# array([[-0.01798621],
	# [-0.07194484]])

	# Example 2:
	y2 = np.array([[1], [0], [1], [0], [1]])
	x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
	theta2 = np.array([[2], [0.5]])
	print(log_gradient(x2, y2, theta2))
	# Output:
	# array([[0.3715235 ],
	# [3.25647547]])

	# Example 3:
	y3 = np.array([[0], [1], [1]])
	x3 = np.array([[0, 2, 3, 4], [2, 4, 5, 5], [1, 3, 2, 7]])
	theta3 = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])
	print(log_gradient(x3, y3, theta3))
	# Output:
	# array([[-0.55711039],
	# [-0.90334809],
	# [-2.01756886],
	# [-2.10071291],
	# [-3.27257351]])

if __name__ == "__main__":
	main()
