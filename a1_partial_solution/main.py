from file_IO import load, save_to_csv, save_to_json
from data_transformation import fill_missing_values, normalize_numeric


# load data
filename = './a1_partial_solution/data/census_dataset.txt'
table = load(filename)

# normalize numeric columns
table = normalize_numeric(table)

# fill missing values
table = fill_missing_values(table)

# save in CSV and JSON formats
save_filename = filename[:-4] + '_transformed'
save_to_csv(table, f'{save_filename}.csv')
save_to_json(table, f'{save_filename}.json')
