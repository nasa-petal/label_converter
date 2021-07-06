# Overview
This repository contains scripts for converting the labels in a CSV file using a label map CSV (like the one titled function_map.csv).

## File descriptions

- **convert_labels**

Takes in a function map and a list of lists of strings (with each list of strings being associated with one paper and the strings being each individual label) and outputs a list of 3 strings (corresponding to lvl 1, 2, and 3 labels respectively)

- **get_function_map**

Converts a function map CSV to a list of 3 lists

- **get_labels**

Takes in a CSV file with all paper info and returns list of lists of strings (labels), with each inner list corresponding to one paper

- **get_paper_info**

Definition of the PaperInfo object

- **labels_to_list**

Turns list of strings into list of lists, with each list containing strings corresponding to functions

- **prepare_csv**

Calls the write_csv function

- **test_get_labels**

Tests the get_labels function

- **write_csv**

Creates a file called output.csv with all of the paper info in the input CSV along with the updated labels
