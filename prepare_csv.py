import argparse
import sys

import get_labels
import get_paper_info
import write_csv

parser = argparse.ArgumentParser(description='Prepare CSV Command Line Tool')

parser.add_argument('input_csv', type=str, help='CSV file from Airtable')

parser.add_argument('output_csv', type=str, help='Updated CSV file')

args = parser.parse_args(sys.argv)  # sys.argv is used if argv parameter is None
input_csv_filename = args.input_csv
output_csv_filename = args.output_csv

labels = get_labels.get_labels(input_csv_filename)
function_map = "function_map.csv"

info_on_papers = []
for label in labels:
    #fix this
    label_one, label_two, label_three = get_paper_info.get_paper_info(labels, function_map)
    info_on_papers.append((label_one, label_two, label_three))

write_csv.write_csv(info_on_papers, output_csv_filename)