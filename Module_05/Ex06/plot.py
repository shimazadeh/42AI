import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
from prediction import predict_
from other_loss import mse_, rmse_, mae_, r2score_

def plot_with_loss(x, y, theta):

	y_predict = predict_(x, theta)

	plt.scatter(x, y, color='blue')
	plt.plot(x, y_predict, color='red')
	for i in range(0, len(y), 1):
		x_values = [x[i], x[i]]
		y_values = [y[i], y_predict[i][0]]
		plt.plot(x_values, y_values, color='red', linestyle="--")

	plt.title(mse_(y, predict_(x, theta)))
	plt.show()

def main():
	x = np.arange(1,6)
	y = np.array([11.52434424, 10.62589482, 13.14755699, 18.60682298, 14.14329568])

	# Example 1:
	theta1 = np.array([[18],[-1]])
	plot_with_loss(x, y, theta1)

	# Example 2:
	theta2 = np.array([[14],[0]])
	plot_with_loss(x, y, theta2)

	# Example 3:
	theta3 = np.array([[12],[0.8]])
	plot_with_loss(x, y, theta3)


if __name__ == "__main__":
	main()
