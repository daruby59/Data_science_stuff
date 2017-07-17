# 
# basic statistical functions
# 
from __future__ import division
import urllib2
import math

# (1)
def mean(x):
    count = len(x)
    sumx = sum(x)
    return sumx/count
# (2)
def data_range(x):
    return max(x) - min(x)
# (3)
def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]
# (4)
def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)
# (5)    
def standard_deviation(x):
    return math.sqrt(variance(x))
# (6)
def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))
# (7)
def sum_of_squares(v):
    return dot(v, v)
# (8)   
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)
# (9)
def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero
# (10)
def predict(alpha, beta, x_i):
    return beta * x_i + alpha
# (11)
def error(alpha, beta, x_i, y_i):
    return y_i - predict(alpha, beta, x_i)
# (12)
def sum_of_squared_errors(alpha, beta, x, y):
    return sum(error(alpha, beta, x_i, y_i) ** 2
               for x_i, y_i in zip(x, y))
# (13)
def least_squares_fit(x,y):
    beta = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
    alpha = mean(y) - beta * mean(x)
    return alpha, beta
# (14)
def total_sum_of_squares(y):
    return sum(v ** 2 for v in de_mean(y))
# (15)
def r_squared(alpha, beta, x, y):
    return 1.0 - (sum_of_squared_errors(alpha, beta, x, y) /
                  total_sum_of_squares(y))
# (16)
def squared_error(x_i, y_i, theta):
    alpha, beta = theta
    return error(alpha, beta, x_i, y_i) ** 2
# (17)
def total_sum_of_squares(y):
    return sum(v ** 2 for v in de_mean(y))
# (18)
def r_squared(alpha, beta, x, y):
    return 1.0 - (sum_of_squared_errors(alpha, beta, x, y) /
                  total_sum_of_squares(y))
#
# end of routines
#
def main():
    daily_minutes = [1,68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,54.01,38.79,47.59,49.1,27.66,41.03,36.73,48.65,28.12,46.62,35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,20.45,21.93,26.02,27.34,23.49,46.94,30.5,33.8,24.23,21.4,27.94,32.24,40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,26.97,36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,36.07,28.66,29.08,37.28,15.28,24.17,22.31,30.17,25.53,19.85,35.37,44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,28.77,24.26,31.98,25.73,24.86,16.28,34.51,15.23,39.72,40.8,26.06,35.76,34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,14.18,35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,27.61,27.21,26.61,29.77,20.59,27.53,13.82,33.2,25,33.1,36.65,18.63,14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,19.42,29.79,32.8,35.99,28.32,27.79,35.88,29.06,36.28,14.1,36.63,37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,32.51,25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,20.42,27.32,18.23,35.35,28.48,9.08,24.62,20.12,35.26,19.92,31.02,16.49,12.16,30.7,31.22,34.65,13.13,27.51,33.2,31.57,14.1,33.42,17.44,10.12,24.42,9.82,23.39,30.93,15.03,21.67,31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]
    num_friends = [100,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    mu = mean(num_friends)
    sigma_sq = variance(num_friends)
    sigma = standard_deviation(num_friends)
    rho = correlation(num_friends,daily_minutes)
    b0, b1 = least_squares_fit(num_friends,daily_minutes)
    rsq = r_squared(b0,b1,num_friends,daily_minutes)
    sse = sum_of_squared_errors(b0,b1,num_friends,daily_minutes)
    sst = total_sum_of_squares(daily_minutes)
    ssr = sst - sse
    #
    msse = sse / (len(num_friends)-2)
    mssr = ssr/1
    msst = sst / (len(num_friends)-1)
    std_error_est = math.sqrt(sse)
    Fstat = mssr/msse
    print "mean: ",mu
    print "variance: ",sigma_sq
    print "standard dev: ",sigma
    print "correlation: ",round(rho,3)
    print "alpha: ",b0," beta: ",b1
    print "r-squared: ",rsq
    print "standard error of the estimate: ",std_error_est
    print "Sum of Squares [errors]: ", sse
    print "Sum of Squares [regression]: ",ssr
    print "Sum of Squares [total]: ",sst
    #
    print "Mean Sum of Squares [errors]: ", msse
    print "Mean Sum of Squares [regression]: ",mssr
    print "Mean Sum of Squares [total]: ",msst
    print "F statistic: ",Fstat
if __name__ == "__main__":
    main()
