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

def main():
	x = np.arange(1, 6)
	print("x before the change: \n" , np.array2string(x, separator=', '))
	x = add_intercept(x)
	print("x after the change: \n" , np.array2string(x, separator=', '))

	y = np.arange(1,10).reshape((3,3))
	print("y before the change: \n" , np.array2string(y, separator=', '))
	y = add_intercept(y)
	print("y after the change: \n" , np.array2string(y, separator=', '))

if __name__ == "__main__":
	main()

# # Example 1:
# x = np.arange(1,6)
# add_intercept(x)
# # Output:
# array([[1., 1.],
# [1., 2.],
# [1., 3.],
# [1., 4.],
# [1., 5.]])

# # Example 2:
# y = np.arange(1,10).reshape((3,3))
# add_intercept(y)
# # Output:
# array([[1., 1., 2., 3.],
# [1., 4., 5., 6.],
# [1., 7., 8., 9.]])
