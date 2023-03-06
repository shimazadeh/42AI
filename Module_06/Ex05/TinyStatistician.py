import numpy as np
import math

class TinyStatistician:
	@staticmethod
	def	mean(x):
		all_sum = 0
		for elements in x:
			all_sum += elements
		return (all_sum/len(x))

	@staticmethod
	def median(x):
		tmp = np.sort(x)
		tmp = np.float_(tmp)
		if (len(tmp) % 2):#if odd number of elements
			return (tmp[int((len(tmp)/2))])
		else:
			return ((tmp[int(len(tmp)/2) - 1] + tmp[int(len(tmp)/2)]) / 2)

	@staticmethod
	def quartile(x):
		tmp = np.sort(x)#sort the list
		tmp = np.float_(tmp)#convert to float
		m_list = [0, 0]
		m_list[0] = tmp[int((len(tmp) + 1) / 4)]
		m_list[1] = tmp[3 * int((len(tmp) + 1) / 4)]
		return (m_list)

	@staticmethod
	def percentile(x, p):
		print("will come back to this later")

	def var(self, x):
		sum = self.mean(x)
		res = 0
		for elements in x:
			res = res + ((elements - sum)) ** 2
		return ((float)(res/(len(x)- 1)))

	def std(self, x):
		sum = self.mean(x)
		res = 0
		for elements in x:
			res = res + (elements - sum) ** 2
		return (math.sqrt(res / (len(x)))) #changing this to population because thats what they want here
