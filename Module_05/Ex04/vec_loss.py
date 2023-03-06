import numpy as np

def loss_(y, y_hat):
	MSE = (np.square(np.subtract(y, y_hat)).mean())/2
	return (MSE)

def main():
	X = np.array([[0], [15], [-9], [7], [12], [3], [-21]])
	Y = np.array([[2], [14], [-13], [5], [12], [4], [-19]])
	print(loss_(X, Y))
	print(loss_(X, X))

if __name__ == "__main__":
	main()
