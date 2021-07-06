import pandas as pd
import get_labels
import get_paper_info


def write_csv(input_csv_filename,function_map_csv, output_csv_filename):
    labels = get_labels.get_labels(input_csv_filename)
    df = pd.read_csv(input_csv_filename)
    for index in df.index:
        paper_info = get_paper_info.get_paper_info(labels[index], function_map_csv)
        df.loc[index, "Functions Level I"] = paper_info[0]
        df.loc[index, "Functions Level II"] = paper_info[1]
        df.loc[index, "Functions Level III- NEW"] = paper_info[2]
    df.to_csv(output_csv_filename, index=False)

write_csv("test_papers.csv", "function_map.csv", "output.csv")