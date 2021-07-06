import pandas as pd


def get_function_map(input_csv_filename):
    # returns function map as a list of 3 lists (lvl 1, lvl 2, and lvl 3 functions)
    df = pd.read_csv(input_csv_filename)
    list_of_lists = [df["Level I"].tolist(), df["Level II"].tolist(), df["Level III"].tolist()]
    return list_of_lists