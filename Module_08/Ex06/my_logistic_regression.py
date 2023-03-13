import numpy as np
import pandas as pd
import math
class MyLogisticRegression():
	"""
	Description:
	My personnal logistic regression to classify things.
	"""
	def __init__(self, theta, alpha=0.001, max_iter=1000):
		self.alpha = alpha
		self.max_iter = max_iter
		self.theta = theta
	# ... Your code here ...
	# ... other methods ...

	def add_intercept(self, x):
		if x is None:
			return 0
		df = pd.DataFrame(x)
		num_columns = len(df.axes[1])
		first_column = df.pop(0)
		df.insert(0, 0, 1)

		i = 1
		while(i < num_columns + 1):
			if (i < num_columns):
				next_column = df.pop(i)
			else:
				next_column = 0
			df.insert(i, i, first_column)
			first_column = next_column
			i = i + 1
		x = df.to_numpy()
		return (x)

	def predict_(self, x):
		x_ = self.add_intercept(x)
		y_ = np.dot(x_, self.theta)
		sig_ = np.zeros((len(y_), 1))
		for i in range(len(y_)):
			sig_[i] = 1 / ( 1 + math.e ** -(y_[i]))
		return (sig_)

	def loss_elem_(self, y, yhat):
		J_ = np.zeros((len(yhat), 1))
		for i in range(len(yhat)):
			J_[i] = y[i] * math.log(yhat[i]) + (1 - y[i]) * math.log(1 - yhat[i])# log to the base of e
		return (-(np.average(J_)))

	def loss_(self, y, yhat):#this is supposed to be ex03 but it doesnt work for now
		eps=1e-15
		J_ = np.zeros((len(yhat), 1))
		for i in range(len(yhat)):
			J_[i] = (y[i]) * math.log(yhat[i]) + (1 - y[i]) * math.log(1 - yhat[i] + eps)# log to the base of e
		return (-(np.average(J_)))

	def log_gradient(self, x, y, theta):
		x_ = self.add_intercept(x)
		x_t = x_.transpose()
		h_ = self.predict_(x)
		m = len(x)
		J_ = np.dot(x_t, (h_ - y))/m
		return (J_)

	def fit_(self, x, y):
		for i in range(self.max_iter):
			delta_j = self.log_gradient(x, y, self.theta)
			for j in range(len(self.theta)):
				self.theta[j] = self.theta[j] - self.alpha * delta_j[j]
		return (self.theta)
