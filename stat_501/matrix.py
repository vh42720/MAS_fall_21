import numpy as np
from sklearn.linear_model import LinearRegression
from utils.matrix_helper import create_matrix

# remove warnings
np.set_printoptions(suppress=True)

# create matrix with helper functions
X_list = [1, 7, 33, 1, 4, 41, 1, 16, 7, 1, 3, 49, 1, 21, 5, 1, 8, 31]
Y_list = [42, 33, 75, 28, 91, 55]
X = create_matrix(X_list, 6, 3)
Y = create_matrix(Y_list, 6, 1)

# TODO: bunch of maths that needs to be sorted
first = np.linalg.inv(X.T * X)
B = first * X.T * Y
Y_hat = X * B
e = Y - Y_hat
MSE = np.sum(np.square(e)) / 3
var_matrix = MSE * (np.linalg.inv(X.T * X))
X_h = np.matrix([[1],
                 [10],
                 [30]])
temp = X_h.T * var_matrix * X_h
print(var_matrix)

X = np.array([[1, 7, 33],
              [1, 4, 41],
              [1, 16, 7],
              [1, 3, 49],
              [1, 21, 5],
              [1, 8, 31]])
reg = LinearRegression().fit(X, Y)
print(reg.coef_)
print(reg.intercept_)
