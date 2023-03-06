import numpy as np

def mse_(y, y_hat):
	MSE = (np.square(np.subtract(y, y_hat)).mean())
	return (MSE)

def rmse_(y, y_hat):
	RMSE = np.sqrt(mse_(y, y_hat))
	return (RMSE)

def mae_(y, y_hat):
	MAE = (np.absolute(np.subtract(y, y_hat))).mean()
	return (MAE)

def r2score_(y, y_hat):
	y_mean = y.mean()
	R2 = 1 - (np.square((np.subtract(y, y_hat))).mean() / np.square(np.subtract(y, y_mean)).mean())

	return (R2)

def main():
	X = np.array([[0], [15], [-9], [7], [12], [3], [-21]])
	Y = np.array([[2], [14], [-13], [5], [12], [4], [-19]])
	print(mse_(X, Y))
	print(rmse_(X, Y))
	print(mae_(X, Y))
	print(r2score_(X, Y))

if __name__ == "__main__":
	main()
