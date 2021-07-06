import get_function_map


def convert_labels(function_map_csv, labels):
    #convert function map into a list of lists
    function_map = get_function_map.get_function_map(function_map_csv)

    #separate each level of labels into its own list to make it easier to understand
    level_one = function_map[0]
    level_two = function_map[1]
    level_three = function_map[2]

    result = ["", "", ""]

    for label in labels:
        index = -1

        # check if label is nan
        if label != label:
            pass

        # check if label is in level 3 of function map
        elif label in level_three:
            index = level_three.index(label)

        # if not found in level 3, check for label level 2 of function map
        elif (len(label) > 0 and label in level_two):
            index = level_two.index(label)

        if index > -1:
            # if statements prevent duplicate labels
            if (result[0].find(level_one[index]) < 0):
                result[0] = result[0] + level_one[index] + ","

            level_two_exists = level_two[index] == level_two[index] # prevents errors if lvl2 is nan
            if (level_two_exists and result[1].find(level_two[index]) < 0):
                result[1] = result[1] + level_two[index] + ","

            level_three_exists = level_three[index] == level_three[index] # prevents errors if lvl3 is nan
            if (level_three_exists and result[2].find(level_three[index]) < 0):
                result[2] = result[2] + level_three[index] + ","

        # for if label is nan
        elif (label != label):
            result[2] = result[2] + ","

        #if label is not found in function map leave as is
        else:
            result[2] = result[2] + label + ","

    # remove the final comma
    result[0] = result[0][0:len(result[0]) - 1]
    result[1] = result[1][0:len(result[1]) - 1]
    result[2] = result[2][0:len(result[2]) - 1]

    return result

# test = [nan]
# test = ["Attach temporarily","Manage compression","Move through/on liquids"]
# print(convert_labels("function_map.csv", test))