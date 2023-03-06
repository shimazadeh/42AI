import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

def plot(x, y, theta):
	plt.scatter(x, y, color='blue')
	plt.plot(x, predict_(x, theta), color='red')
	plt.show()

def main():
	x = np.arange(1,6)
	y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])

	# Example 1:
	theta1 = np.array([[4.5],[-0.2]])
	plot(x, y, theta1)

	# Example 2:
	theta2 = np.array([[-1.5],[2]])
	plot(x, y, theta2)

	# Example 3:
	theta3 = np.array([[3],[0.3]])
	plot(x, y, theta3)


if __name__ == "__main__":
	main()
