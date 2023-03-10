
import numpy as np
from polynomial_model import add_polynomial_features
from mylinearregression import MyLinearRegression as MyLR
import matplotlib.pyplot as plt
import pandas as pd

# def main():
# 	data = pd.read_csv("are_blue_pills_magics (1).csv")

# 	x = np.array(data["Patient"])
# 	y = np.array(data["Score"])


# 	print(x)
# 	# Build the model:
# 	x_4 = add_polynomial_features(np.array(data["Patient"]).reshape(-1, 1), 4)
# 	print(x_4)
# 	theta4 = np.array([[-20],[ 160],[ -80],[ 10],[ -1]]).reshape(-1,1)
# 	my_lr = MyLR(theta4)
# 	my_lr.fit_(x_4.reshape(-1, 1), y)
# 	y_pred4 = my_lr.predict_(x_4)

# 	print(y_pred4)
# 	# Plot:
# 	## To get a smooth curve, we need a lot of data points
# 	# continuous_x = np.arange(1,10.01, 0.01).reshape(-1,1)
# 	# x_ = add_polynomial_features(continuous_x, 3)
# 	# y_hat = my_lr.predict_(continuous_x)
# 	plt.scatter(x,y)
# 	plt.plot(x_4, y_pred4, color="orange")
# 	plt.show()




def main():
	x = np.arange(1,11).reshape(-1,1)
	y = np.array([[ 1.39270298],
	[ 3.88237651],
	[ 4.37726357],
	[ 4.63389049],
	[ 7.79814439],
	[ 6.41717461],
	[ 8.63429886],
	[ 8.19939795],
	[10.37567392],
	[10.68238222]])

	# Build the model:
	x_ = add_polynomial_features(x, 3)
	my_lr = MyLR(thetas=np.ones(4).reshape(-1, 1))
	my_lr.fit_(x_, y)

	# Plot:
	## To get a smooth curve, we need a lot of data points
	continuous_x = np.arange(1,10.01, 0.01).reshape(-1, 1)
	x_ = add_polynomial_features(continuous_x, 3)

	print("x is \n" ,x_)
	print("theta is \n", my_lr.thetas)
	y_hat = my_lr.predict_(x_)
	print(y_hat)

	plt.scatter(x,y)
	plt.plot(continuous_x, y_hat, color="orange")
	plt.show()

if __name__ == "__main__":
	main()
