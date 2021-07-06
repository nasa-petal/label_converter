import convert_labels
import get_function_map


class PaperInfo(object):
    def __init__(self, orig_functions, function_map):
        self.orig_functions = orig_functions
        self.function_map = get_function_map.get_function_map(function_map)
        self.new_functions = convert_labels.convert_labels(function_map, self.orig_functions)

    def get_label_one(self):
        return self.new_functions[0]

    def get_label_two(self):
        return self.new_functions[1]

    def get_label_three(self):
        return self.new_functions[2]


def get_paper_info(orig_functions, function_map):
    paper_info_instance = PaperInfo(orig_functions, function_map)

    #Retrieiving labels of each level
    level_one = paper_info_instance.get_label_one()
    level_two = paper_info_instance.get_label_two()
    level_three = paper_info_instance.get_label_three()

    return level_one, level_two, level_three

# print(get_paper_info(["Manage impact"], "function_map.csv"))
# print(get_paper_info(["Manage impact","Move through/on liquids", "Detox/purify"], "function_map.csv"))