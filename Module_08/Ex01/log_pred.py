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

def main():
	# Example 1
	x = np.array([4]).reshape((-1, 1))
	theta = np.array([[2], [0.5]])
	print(logistic_predict_(x, theta))
	# Output:
	# array([[0.98201379]])

	# Example 2
	x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
	theta2 = np.array([[2], [0.5]])
	print(logistic_predict_(x2, theta2))
	# Output:
	# array([[0.98201379],
	# [0.99624161],
	# [0.97340301],
	# [0.99875204],
	# [0.90720705]])

	# Example 3
	x3 = np.array([[0, 2, 3, 4], [2, 4, 5, 5], [1, 3, 2, 7]])
	theta3 = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])
	print(logistic_predict_(x3, theta3))
	# Output:
	# array([[0.03916572],
	# [0.00045262],
	# [0.2890505 ]])

if __name__ == "__main__":
	main()
