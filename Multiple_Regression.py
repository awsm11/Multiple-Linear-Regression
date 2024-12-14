import numpy as np
from matrix import excel_data, m, n, y_1
from input_algorthm import input_function


# The function is responsible for calculating the value of the cost function
def compute_cost(x, y, w, b):

    total_error = 0

    for i in range(len(excel_data)):
        # f_wb is representing the model function
        f_wb = np.dot(x[i], w) + b
        error = (f_wb - y[i]) ** 2
        total_error += error

    j_wb = total_error / (2 * m)
    return j_wb


# Calculations of the differential values of the cost function are used to determine the gradient
def compute_gradient(x, y, w, b):

    total_error_w = np.zeros((n, ))
    total_error_b = 0

    for i in range(m):
        error = (np.dot(x[i], w) + b) - y[i]
        for j in range(n):
            total_error_w[j] = total_error_w[j] + error * x[i, j]
        total_error_b += error
    dev_jw = total_error_w / m
    dev_jb = total_error_b / m

    return dev_jw, dev_jb


# Gradient descent function with respect to number of iteration
def gradient_descent(iteration, x, y, w_in, b_in, alpha, cost_calculation, gradient_calculation):

    j_wb_storage = []
    w_storage = []
    b_storage = []
    w = w_in
    b = b_in

    # Parameters w, b calculation by evaluating the iteration number
    for i in range(iteration):
        dev_jw, dev_jb = gradient_calculation(x, y, w, b)
        w = w - alpha * dev_jw
        b = b - alpha * dev_jb
        b_storage.append(b)
        w_storage.append(w)
        j_wb_storage.append(cost_calculation(x, y, w, b))

    w_storage = np.array(w_storage)

    j_wb_storage_min = np.min(j_wb_storage)
    for i in range(iteration):
        if j_wb_storage[i] == j_wb_storage_min:

            # Determining of parameters w and b values at point where error is minimized
            w_model = w_storage[i]
            b_model = b_storage[i]
            print("w_model = {} and b_model = {}".format(w_model, b_model))

            # The function allows user to input values representing the characteristics of the home they are looking for
            input_function(w_model[0], w_model[1], w_model[2], w_model[3], b_model)

    return w, b, j_wb_storage


# The initial parameters that we choose to start the optimization process
initial_w = np.array([0, 0, 0, 0])
initial_b = 0

# Number of descent
iterations = 5000

# The learning rate adjusted to be more appropriate for our normalized data values
alpha = 0.1

gradient_descent(iterations, excel_data, y_1, initial_w, initial_b, alpha, compute_cost, compute_gradient)