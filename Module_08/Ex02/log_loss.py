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

def log_loss_(y, y_hat, eps=1e-15):
	"""
	Computes the logistic loss value.
	Args:
	y: has to be an numpy.ndarray, a vector of shape m * 1.
	y_hat: has to be an numpy.ndarray, a vector of shape m * 1.
	eps: has to be a float, epsilon (default=1e-15)
	Returns:
	The logistic loss value as a float.
	None on any error.
	Raises:
	This function should not raise any Exception.
	"""
	J_ = np.zeros((len(y_hat), 1))
	for i in range(len(y_hat)):
		J_[i] = y[i] * math.log(y_hat[i]) + (1 - y[i]) * math.log(1 - y_hat[i])
	return (-(np.average(J_)))

def main():
	# Example 1:
	y1 = np.array([1]).reshape((-1, 1))
	x1 = np.array([4]).reshape((-1, 1))
	theta1 = np.array([[2], [0.5]])
	y_hat1 = logistic_predict_(x1, theta1)
	print(log_loss_(y1, y_hat1))
	# Output:
	# 0.01814992791780973

	# Example 2:
	y2 = np.array([[1], [0], [1], [0], [1]])
	x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
	theta2 = np.array([[2], [0.5]])
	y_hat2 = logistic_predict_(x2, theta2)
	print(log_loss_(y2, y_hat2))
	# Output:
	# 2.4825011602474483

	# Example 3:
	y3 = np.array([[0], [1], [1]])
	x3 = np.array([[0, 2, 3, 4], [2, 4, 5, 5], [1, 3, 2, 7]])
	theta3 = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])
	y_hat3 = logistic_predict_(x3, theta3)
	print(log_loss_(y3, y_hat3))
	# Output:
	# 2.9938533108607053

if __name__ == "__main__":
	main()
