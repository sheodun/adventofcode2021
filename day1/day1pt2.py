file = open("data", "r")
data = file.readlines()

# Convert the data to integers.
depths = list(map(int, data))

nincreases = 0
previous_alt = sum(depths[0:3])
for index, alt in enumerate(depths):
	uindex = index + 3
	alt_sum = sum(depths[index:uindex])
	if (alt_sum - previous_alt) > 0:
		nincreases += 1
	previous_alt = alt_sum

output = "Number of increases: {0}".format(nincreases)
print(output)