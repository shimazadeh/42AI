
import numpy as np

def add_polynomial_features(x, power):
	y = np.zeros((len(x),power), dtype = int)
	for i in range(len(x)):
		for j in range(power):
			if j == 0:
				y[i][j] = x[i][j]
			else:
				y[i][j] = x[i][0] ** (j + 1)
	return (y)



