import numpy as np
import math

def sigmoid_(x):
	"""
	Compute the sigmoid of a vector.
	Args:
	x: has to be a numpy.ndarray of shape (m, 1).
	Returns:
	The sigmoid value as a numpy.ndarray of shape (m, 1).
	None if x is an empty numpy.ndarray.
	Raises:
	This function should not raise any Exception.
	"""
	sig_ = np.zeros((len(x), 1))
	for i in range(len(x)):
		sig_[i] = 1 / ( 1 + math.e ** -(x[i]))
	return (sig_)


def main():
	x = np.array([[-4]])
	print(sigmoid_(x))
	# Output:
	# array([[0.01798620996209156]])
	# Example 2:
	x = np.array([[2]])
	print(sigmoid_(x))
	# Output:
	# array([[0.8807970779778823]])
	# Example 3:
	x = np.array([[-4], [2], [0]])
	print(sigmoid_(x))
	# Output:
	# array([[0.01798620996209156], [0.8807970779778823], [0.5]])


if __name__ == "__main__":
	main()
