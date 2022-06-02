from Common import constants, counter
import pandas as pd

# Extract data with idx
def extract_data(base):
    columns = constants.all_col
    first_idx = counter.read(base) #first row to read
    last_idx = first_idx+constants.row_to_map #last row to read
    if base=='Adult.data':
        data = pd.read_csv(f'../data/{base}', sep=",", skipinitialspace=True, names=columns, index_col=False, skiprows=lambda x: x not in range(first_idx, last_idx))
    elif base=='Adult.test':
        data = pd.read_csv(f'../data/{base}', sep=",", skipinitialspace=True, names=columns, index_col=False, skiprows=lambda x: x not in range(first_idx, last_idx))
    return data, last_idx