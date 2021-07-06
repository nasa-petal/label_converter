import pandas as pd
import labels_to_list


def get_labels(input_csv_filename):
    # returns list of lists of strings (labels), with each inner list corresponding to one paper
    df = pd.read_csv(input_csv_filename)
    functions = df["Functions Level III- NEW"].tolist()
    return labels_to_list.labels_to_list(functions)