import numpy as np
import math
import pandas as pd
from tools import add_intercept

def predict_(x, theta):
	if x is None or theta is None:
		return 0
	z = add_intercept(x)
	if (len(pd.DataFrame(z).axes[1]) != len(theta)):
		return 0
	return (np.dot(z, theta))
