import numpy as np
import sys

lambda_input = int(sys.argv[1])
sigma2_input = float(sys.argv[2])
X_train = np.genfromtxt(sys.argv[3], delimiter = ",")
y_train = np.genfromtxt(sys.argv[4])
X_test = np.genfromtxt(sys.argv[5], delimiter = ",")

## Solution for Part 1
def part1(train, label, lambda_input):
    
    ## Input : Arguments to the function
    ## Return : wRR, Final list of values to write in the file
    
    return wrr

wRR = part1(X_train, y_train, lambda_input)  # Assuming wRR is returned from the function
np.savetxt("wRR_" + str(lambda_input) + ".csv", wRR, delimiter="\n") # write output to file

## Solution for Part 2
def part2(train, test, lambda_input, sigma2):
        
    return locations
    ## Input : Arguments to the function
    ## Return : active, Final list of values to write in the file
    

active = part2(X_train,X_test, lambda_input, sigma2_input)  # Assuming active is returned from the function
np.savetxt("active_" + str(lambda_input) + "_" + str(int(sigma2_input)) + ".csv", active, delimiter=",") # write output to file
