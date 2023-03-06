import numpy as np
import math
import pandas as pd

def predict_(x, theta):
	if x is None or theta is None:
		return 0
	z = add_intercept(x)
	if (len(pd.DataFrame(z).axes[1]) != len(theta)):
		return 0
	return (np.dot(z, theta))

def main():
	x = np.arange(1,6)

	theta1 = np.array([[5], [0]])
	print("Example2: \n", predict_(x, theta1))

	theta2 = np.array([[0], [1]])
	print("Example2: \n", predict_(x, theta2))

	theta3 = np.array([[5], [3]])
	print("Example3: \n", predict_(x, theta3))

	theta4 = np.array([[-3], [1]])
	print("Example4: \n", predict_(x, theta4))


if __name__ == "__main__":
	main()
