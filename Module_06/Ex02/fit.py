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

def	gradient(x, y, theta):
	if theta is None or x is None or y is None:
		return 0
	if len(x) != len(y):
		return 0
	x_new = add_intercept(x)
	x_t = np.transpose(x_new)
	m = len(x_new)
	J = (np.dot(x_new, theta) - y)/len(x)
	J = np.dot(x_t, J)
	return (J)

def	fit_(x, y, theta, alpha, max_iter):
	if theta is None or x is None or y is None:
		return 0
	if len(x) != len(y):
		return 0
	for i in range(max_iter):
		delta_j = gradient(x, y, theta)
		theta[0] = theta[0] - alpha * delta_j[0]
		theta[1] = theta[1] - alpha * delta_j[1]
	return (theta)

def	main():
	x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
	y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
	theta = np.array([1.00, 1.00]).reshape((-1, 1))

	# Example 0:
	theta1 = fit_(x, y, theta, alpha=5e-8, max_iter=1500000)
	print(theta1)
	# theta1
	# Output:
	# array([[1.40709365],[1.1150909 ]])

	# Example 1:
	# predict(x, theta1)
	# Output:
	# array([[15.3408728 ],
	# [25.38243697],
	# [36.59126492],
	# [55.95130097],
	# [65.53471499]])

if __name__ == "__main__":
	main()
