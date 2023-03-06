import numpy as np

def	simple_gradient(x, y, theta):
	if theta is None or x is None or y is None:
		return 0
	if len(x) != len(y):
		return 0
	m = len(x)
	J = np.array([0.0, 0.0])
	for i in range(m):
		J[0] = J[0] + ((theta[0] + theta[1] * x[i]) - y[i])/m
		J[1] = J[1] + ((theta[0] + theta[1] * x[i]) - y[i]) * x[i]/m
	return (J)

def	main():
	x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733]).reshape((-1, 1))
	y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554]).reshape((-1, 1))
	# Example 0:
	theta1 = np.array([2, 0.7]).reshape((-1, 1))
	print(simple_gradient(x, y, theta1))
	# Output:
	# array([[-19.0342574], [-586.66875564]])
	# Example 1:
	theta2 = np.array([1, -0.4]).reshape((-1, 1))
	print(simple_gradient(x, y, theta2))
	# Output:
	# array([[-57.86823748], [-2230.12297889]])

if __name__ == "__main__":
	main()
