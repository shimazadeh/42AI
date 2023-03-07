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

def main():
	x = np.arange(1,13).reshape((4,-1))
	# Example 1:
	theta1 = np.array([5, 0, 0, 0]).reshape((-1, 1))
	print(simple_predict(x, theta1))
	# Ouput:
	# array([[5.], [5.], [5.], [5.]])

	# Do you understand why y_hat contains only 5’s here?


	# Example 2:
	theta2 = np.array([0, 1, 0, 0]).reshape((-1, 1))
	print(simple_predict(x, theta2))
	# Output:
	# array([[ 1.], [ 4.], [ 7.], [10.]])
	# Do you understand why y_hat == x[:,0] here?


	# Example 3:
	theta3 = np.array([-1.5, 0.6, 2.3, 1.98]).reshape((-1, 1))
	print(simple_predict(x, theta3))
	# Output:
	# array([[ 9.64], [24.28], [38.92], [53.56]])

	# Example 4:
	theta4 = np.array([-3, 1, 2, 3.5]).reshape((-1, 1))
	print(simple_predict(x, theta4))
	# Output:
	# array([[12.5], [32. ], [51.5], [71. ]])

if __name__ == "__main__":
	main()
