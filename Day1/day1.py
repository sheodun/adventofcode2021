file = open("data", "r")
data = file.readlines()

# Convert the data to integers.
depths = list(map(int, data))

nincreases = 0
previous_alt = depths[0]
for alt in depths:
	if (alt - previous_alt) > 0:
		nincreases += 1
	previous_alt = alt

output = "Number of increases: {0}".format(nincreases)
print(output)