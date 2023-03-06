import pandas as pd
import numpy as np
# from sklearn.metrics import mean_squared_error
from my_linear_regression import MyLinearRegression as MyLR
import matplotlib.pyplot as plt

def main():
	data = pd.read_csv("are_blue_pills_magics.csv")
	Xpill = np.array(data["Micrograms"]).reshape(-1,1)
	Yscore = np.array(data["Score"]).reshape(-1,1)
	linear_model1 = MyLR(np.array([[89.0], [-8]]))
	linear_model2 = MyLR(np.array([[89.0], [-6]]))
	Y_model1 = linear_model1.predict_(Xpill)
	Y_model2 = linear_model2.predict_(Xpill)

	plt.scatter(Xpill, Yscore, color='deepskyblue')
	plt.scatter(Xpill, Y_model1, color='limegreen')
	plt.xlabel("Quantity of blue pill (in micrograms)")
	plt.ylabel("Space driving score")
	plt.show()

	plt.plot()
	print(MyLR.mse_(Yscore, Y_model1))
	# 57.60304285714282
	# print(mean_squared_error(Yscore, Y_model1))
	# 57.603042857142825
	print(MyLR.mse_(Yscore, Y_model2))
	# 232.16344285714285
	# print(mean_squared_error(Yscore, Y_model2))
	# 232.16344285714285

if __name__ == "__main__":
	main()
