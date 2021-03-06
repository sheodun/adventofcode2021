import numpy as np


def convert_binary2int(value):

    if value[0:3] == "0b":
        binary = "0b" + value
    else:
        binary = value

    return int(binary, 2)


f = open("data.txt", "r")
data = f.readlines()
ncol = len(data[0].strip())

gamma_bin = "0b"
epsilon_bin = "0b"

for j in range(ncol):
    n0 = 0
    n1 = 0
    for i in range(len(data)):
        if data[i][j] == "1":
            n1 += 1
        elif data[i][j] == "0":
            n0 += 1

    if n0 > n1:
        gamma_bin += "0"
        epsilon_bin += "1"
    else:
        gamma_bin += "1"
        epsilon_bin += "0"

gaval = convert_binary2int(gamma_bin)
epval = convert_binary2int(epsilon_bin)
print(gamma_bin, epsilon_bin)
print(gaval, epval)
print(gaval * epval)
