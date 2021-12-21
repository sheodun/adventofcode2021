
def oxygen_gen(data):
    """Returns the oxygen generator rating

    Parameters
    ----------
    data : list
        The list of data strings.
    
    Returns
    -------
    str
    """
    ncols = len(data[0])

    numbers = data
    init = False
    for j in range(ncols):
        n0 = 0
        n1 = 0

        # If only 1 number exists in the list,
        # then return it.
        if len(numbers) == 1:
            return numbers[0]

        for item in numbers:
            if item[j] == "1":
                n1 += 1
            elif item[j] == "0":
                n0 += 1

        new_list = []
        for index, item in enumerate(numbers):
            if item[j] == "0" and n0 > n1:
                new_list.append(item)
            elif item[j] == "1" and n1 >= n0:
                new_list.append(item)

        numbers = new_list


def co2_gen(data):
    """Returns the oxygen generator rating                                                                                                                                                               

    Parameters                                                                                                                                                                                               ----------                                                                                                                                                                                               data : list                                                                                                                                                                                          
        The list of data strings.                                                                                                                                                                                                                                                                                                                                                                                 
    Returns                                                                                                                                                                                              
    -------                                                                                                                                                                                              
    str                                                                                                                                                                                                  
    """
    ncols = len(data[0])

    numbers = data
    init = False
    for j in range(ncols):
        n0 = 0
        n1 = 0

        # If only 1 number exists in the list,                                                                                                                                                            
        # then return it.                                                                                                                                                                                 
        if len(numbers) == 1:
            return numbers[0]

        for item in numbers:
            if item[j] == "1":
                n1 += 1
            elif item[j] == "0":
                n0 += 1

        new_list = []
        for index, item in enumerate(numbers):
            if item[j] == "0" and n0 <= n1:
                new_list.append(item)
            elif item[j] == "1" and n1 < n0:
                new_list.append(item)

        numbers = new_list
      

f = open("data.txt", "r")
data = f.readlines()

ox = int(oxygen_gen(data), 2)
co2 = int(co2_gen(data), 2)
print(ox, co2, ox * co2)
