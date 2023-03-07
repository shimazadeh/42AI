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

def	predict_(x, theta):
	if x is None or theta is None:
		return 0
	z = add_intercept(x)
	if (len(pd.DataFrame(z).axes[1]) != len(theta)):
		return 0
	return (np.dot(z, theta))

def gradient(x, y, theta):
	if x is None or y is None or theta is None:
		return 0
	if len(x) != len(y):
		return 0
	x_new = add_intercept(x)
	x_t = np.transpose(x_new)
	m = len(x_new)
	delta_J = (np.dot(x_new, theta) - y) / m # this should be x_new not x to match the method in module06
	delta_J = np.dot(x_t, delta_J)
	return (delta_J)

def fit_(x, y, theta, alpha, max_iter):
	if theta is None or x is None or y is None:
		return 0
	if (len(x) != len(y)):
		return 0
	for i in range(max_iter):
		delta_j = gradient(x, y, theta)
		for j in range(len(theta)):
			theta[j] = theta[j] - alpha * delta_j[j]
	return (theta)
	"""
	Description:
	Fits the model to the training dataset contained in x and y.
	Args:
	x: has to be a numpy.array, a matrix of dimension m * n:
	(number of training examples, number of features).
	y: has to be a numpy.array, a vector of dimension m * 1:
	(number of training examples, 1).
	theta: has to be a numpy.array, a vector of dimension (n + 1) * 1:
	(number of features + 1, 1).
	alpha: has to be a float, the learning rate
	max_iter: has to be an int, the number of iterations done during the gradient descent
	Return:
	new_theta: numpy.array, a vector of dimension (number of features + 1, 1).
	None if there is a matching dimension problem.
	None if x, y, theta, alpha or max_iter is not of expected type.
	Raises:
	This function should not raise any Exception.
	"""

def main():
	x = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
	y = np.array([[19.6], [-2.8], [-25.2], [-47.6]])
	theta = np.array([[42.], [1.], [1.], [1.]])
	# Example 0:
	theta2 = fit_(x, y, theta, alpha = 0.0005, max_iter=42000)
	print(theta2)
	# Output:
	# array([[41.99..],[0.97..], [0.77..], [-1.20..]])

	# Example 1:
	print(predict_(x, theta2))
	# Output:
	# array([[19.5992..], [-2.8003..], [-25.1999..], [-47.5996..]])

if __name__ == "__main__":
	main()
