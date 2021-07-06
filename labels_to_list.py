def labels_to_list(functions): #turns list of strings into list of lists, with each list containing strings corresponding to functions
    result = [];
    for x in functions:
        if (x == x):
            stop = x.find(",")
        else:
            stop = -1
        temp_list = []
        while stop > -1:
            temp_list.append(x[0:stop])
            x = x[stop + 1:]
            stop = x.find(",")
        temp_list.append(x)
        result.append(temp_list)
    return result