import numpy as np
from mylinearregression import MyLinearRegression as MyLR

def	main():
	X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [34., 55., 89., 144.]])
	Y = np.array([[23.], [48.], [218.]])
	mylr = MyLR([[1.], [1.], [1.], [1.], [1]])
	# Example 0:
	y_hat = mylr.predict_(X)
	print(y_hat)
	# Output:
	# array([[8.], [48.], [323.]])

	# Example 1:
	print(mylr.loss_elem_(Y, y_hat))
	# Output:
	# array([[225.], [0.], [11025.]])

	# Example 2:
	print(mylr.loss_(Y, y_hat))
	# Output:
	# 1875.0

	# Example 3:
	mylr.alpha = 1.6e-4
	mylr.max_iter = 200000
	print(mylr.fit_(X, Y))
	# Output:
	# array([[18.188..], [2.767..], [-0.374..], [1.392..], [0.017..]])

	# Example 4:
	y_hat = mylr.predict_(X)
	print(y_hat)
	# Output:
	# array([[23.417..], [47.489..], [218.065...]])

	# Example 5:
	print(mylr.loss_elem_(Y, y_hat))
	# Output:
	# array([[0.174..], [0.260..], [0.004..]])

	# Example 6:
	print(mylr.loss_(Y, y_hat))
	# Output: 0.0732

if __name__ == "__main__":
	main()
