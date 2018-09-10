import numpy as np
import sys

lambda_input = int(sys.argv[1])
sigma2_input = float(sys.argv[2])
X_train = np.genfromtxt(sys.argv[3], delimiter = ",")
y_train = np.genfromtxt(sys.argv[4])
X_test = np.genfromtxt(sys.argv[5], delimiter = ",")

## Solution for Part 1
def part1(train, label, lambda_input):
    train_t = train.T
    identity = np.eye(len(train_t), dtype = float)
    xtx = np.dot(train_t,train)
    li = lambda_input*identity
    invers = np.linalg.inv(xtx + li)
    xty = np.dot(train_t,label)
    ixt = np.dot(invers, xtx)
    wrr = np.dot(invers, xty)
    ## Input : Arguments to the function
    ## Return : wRR, Final list of values to write in the file
    
    return wrr

wRR = part1(X_train, y_train, lambda_input)  # Assuming wRR is returned from the function
np.savetxt("wRR_" + str(lambda_input) + ".csv", wRR, delimiter="\n") # write output to file

## Solution for Part 2
def part2(train, test, lambda_input, sigma2):
    locations = []
    i = 0
    while i != 10:
        max_location = 0
        train_t = train.T
        identity = np.eye(len(train_t), dtype = float)
        xtx = np.dot(train_t,train)
        li = lambda_input*identity
        sigma = np.linalg.inv(li + sigma2*xtx)
        max_sigma = sigma + train[0].T*sigma*train[0]
        for location, x in enumerate(test):
            sigma0 =sigma + x.T*sigma*x
            if sigma0 > max_sigma:
                max_sigma = sigma0
                max_location = location
        locations.append(max_location)
        tran.append(test[max_location])
        np.delete(test,max_location)
        i += 1    
    return locations
    ## Input : Arguments to the function
    ## Return : active, Final list of values to write in the file
    

active = part2(X_train,X_test, lambda_input, sigma2_input)  # Assuming active is returned from the function
np.savetxt("active_" + str(lambda_input) + "_" + str(int(sigma2_input)) + ".csv", active, delimiter=",") # write output to file
