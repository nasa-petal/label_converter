import argparse
import csv
import pandas as pd
import ast

def get_label_map(label_map_file):
    label_map_2_levels = {}
    label_map_3_levels = {}
    with open(label_map_file, encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['label_level_3']:
                label_map_3_levels[row['label_level_3']] = (row['label_level_1'],row['label_level_2'])
            else:
                label_map_2_levels[row['label_level_2']] = row['label_level_1']

    return label_map_2_levels, label_map_3_levels


parser = argparse.ArgumentParser(description='Prepare CSV Command Line Tool')

parser.add_argument('input_csv', type=str, help='CSV file with paper info')

parser.add_argument('label_map_csv', type=str, help='CSV file mapping between levels')

parser.add_argument('output_csv', type=str, help='Updated paper CSV file')

args = parser.parse_args()  # sys.argv is used if argv parameter is None
input_csv_filename = args.input_csv
label_map_csv_filename = args.label_map_csv
output_csv_filename = args.output_csv

label_map_2_levels, label_map_3_levels = get_label_map(label_map_csv_filename)

df_input = pd.read_csv(input_csv_filename)
df_input = df_input.fillna("")

for index, row in df_input.iterrows():
    if row['label_level_3']:
        labels_level_3 = ast.literal_eval(row['label_level_3'])
        labels_level_1 = set()
        if row['label_level_2'] == "":
            labels_level_2_old = []
        else:
            labels_level_2_old = ast.literal_eval(row['label_level_2'])
        labels_level_2 = set()
        for label_level_2 in labels_level_2_old:
            if label_level_2 in label_map_2_levels:
                label_level_1 = label_map_2_levels[label_level_2]
                labels_level_2.add(label_level_2)
                labels_level_1.add(label_level_1)
        for label_level_3 in labels_level_3:
            if label_level_3 in label_map_3_levels:
                label_level_1, label_level_2 = label_map_3_levels[label_level_3]
                labels_level_1.add(label_level_1)
                labels_level_2.add(label_level_2)
            else:
                print(f"This level 3 label is missing from the mapping file: '{label_level_3}'")

        df_input.at[index, 'label_level_1'] = list(labels_level_1)
        df_input.at[index, 'label_level_2'] = list(labels_level_2)
    elif row['label_level_2']:
        labels_level_2 = ast.literal_eval(row['label_level_2'])
        labels_level_1 = set()
        for label_level_2 in labels_level_2:
            if label_level_2 in label_map_2_levels:
                label_level_1 = label_map_2_levels[label_level_2]
                labels_level_1.add(label_level_1)
            else:
                print(f"This level 2 label, found in index {index}, is not a special level 2 label: '{label_level_2}'")
        if not labels_level_1:
            print(f"No level 3 or special level 2 label found in index {index}")
    else:
        labels_level_1 = set()
        print(f"WARNING: Both levels 2 and 3 missing from index {index}")

    df_input.at[index, 'label_level_1'] = list(labels_level_1)



df_input.to_csv(output_csv_filename)
