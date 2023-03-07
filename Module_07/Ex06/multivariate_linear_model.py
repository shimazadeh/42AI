import pandas as pd
import numpy as np
from mylinearregression import MyLinearRegression as MyLR
import matplotlib.pyplot as plt

def multivariate_linear_model():
	data = pd.read_csv("spacecraft_data.csv")

	#=============== prediction by age ===========================
	X1 = np.array(data[["Age"]])
	Y = np.array(data[["Sell_price"]])
	myLR_age = MyLR(thetas = [[1000.0], [-1.0]], alpha = 2.5e-5, max_iter = 100000)
	myLR_age.fit_(X1[:,0].reshape(-1,1), Y)
	y_pred1 = myLR_age.predict_(X1[:,0].reshape(-1,1))
	print(myLR_age.mse_(y_pred1,Y))

	plt.subplots(1)
	plt.scatter(X1, Y, color='blue')
	plt.scatter(X1, y_pred1, color='deepskyblue')
	plt.xlabel("x1: age (in years)")
	plt.ylabel("y: Sell price (in keuros)")

	#=============== prediction by thrust ===========================
	X2 = np.array(data[["Thrust_power"]])
	myLR_thrust = MyLR(thetas = [[0], [1.0]], alpha = 2.5e-5, max_iter = 100000)
	myLR_thrust.fit_(X2[:,0].reshape(-1,1), Y)
	y_pred2 = myLR_thrust.predict_(X2[:,0].reshape(-1,1))
	print(myLR_thrust.mse_(y_pred2,Y))

	plt.subplots(1)
	plt.scatter(X2, Y, color='green')
	plt.scatter(X2, y_pred2, color='lime')
	plt.xlabel("x2: thrust power (in 10Km/s)")
	plt.ylabel("y: Sell price (in keuros)")

	#=============== prediction by total distance ===========================
	X3 = np.array(data[["Terameters"]])
	myLR_dist = MyLR(thetas = [[700.0], [1.0]], alpha = 2.5e-5, max_iter = 100000)
	myLR_dist.fit_(X3[:,0].reshape(-1,1), Y)
	y_pred3 = myLR_dist.predict_(X3[:,0].reshape(-1,1))
	print(myLR_dist.mse_(y_pred3, Y))

	plt.subplots(1)
	plt.scatter(X3, Y, color='purple')
	plt.scatter(X3, y_pred3, color='pink')
	plt.xlabel("x3: distance totalizer value of spacecraft (in Tmeters)")
	plt.ylabel("y: Sell price (in keuros)")
	plt.show()


	#Output
	# 55736.86719...


def main():
	data = pd.read_csv("spacecraft_data.csv")
	X = np.array(data[["Age", "Thrust_power", "Terameters"]])
	Y = np.array(data[["Sell_price"]])
	myLR_all = MyLR(thetas = [1.0, 1.0, 1.0, 1.0], alpha = 1e-4, max_iter = 100)
	y_pred = myLR_all.predict_(X)

	print(myLR_all.mse_(y_pred ,Y))


	myLR_all.fit_(X, Y)
	print(myLR_all.thetas)

	plt.subplots(1)
	plt.scatter(X[:, 0], Y, color='blue')
	plt.scatter(X[:, 0], y_pred, s = 10, color='deepskyblue')
	plt.xlabel("x1: age (in years)")
	plt.ylabel("y: Sell price (in keuros)")


	plt.subplots(1)
	plt.scatter(X[:, 1], Y, color='green')
	plt.scatter(X[:, 1], y_pred, s = 10, color='lime')
	plt.xlabel("x2: thrust power (in 10Km/s)")
	plt.ylabel("y: Sell price (in keuros)")


	plt.subplots(1)
	plt.scatter(X[:, 2], Y, color='purple')
	plt.scatter(X[:, 2], y_pred, s = 10, color='pink')
	plt.xlabel("x3: distance totalizer value of spacecraft (in Tmeters)")
	plt.ylabel("y: Sell price (in keuros)")


	plt.show()
	# print(myLR_all.theta)
	# print(myLR_all.mse_(X ,Y))

	# plt.scatter(X, Y, color='purple')
	# plt.scatter(X, y_pred, color='pink')
	# plt.xlabel("multi_variate_linear_model")
	# plt.ylabel("y: Sell price (in keuros)")
	# plt.show()



if __name__ == "__main__":
	main()
