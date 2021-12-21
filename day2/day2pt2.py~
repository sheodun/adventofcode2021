# Day2 Part 1
from position import Position


# Get data from data.txt
f = open("data.txt")

pos = Position()

for instruction in f.readlines():
    try:
        pos.command(instruction)
    except:
        print(instruction)

print(pos.product())
