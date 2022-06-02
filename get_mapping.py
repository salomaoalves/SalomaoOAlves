import pandas as pd

# Categorical columns
encode_col = ["workclass","education","marital-status","occupation","relationship ","race","sex","native-country","class"]

# Extract data
def extract_data(base):
    columns = ["age","workclass","fnlwgt","education","education-num","marital-status","occupation","relationship ","race","sex","capital-gain","capital-loss","hours-per-week","native-country","class"]
    if base=='Adult.data':
        data = pd.read_csv(f'data/{base}', sep=",\s",names=columns, index_col=False)
    elif base=='Adult.test':
        data = pd.read_csv(f'data/{base}', sep=",\s",names=columns, index_col=False, skiprows=1)
    return data

# Get dict label encoder values for mapping (in str format)
def get_str_mapping(base):
    data = extract_data(base)
    dict_str='dict_map_'+base.split('.')[1]+' = {'
    for col in encode_col:
        dict_str = dict_str+'\n\t"'+str(col)+'": '+str([value for value in list(data[col].sort_values().unique())])+','
    dict_str = dict_str[:-1] + '\n}'
    return dict_str

def main():
    print('Mapping for Adult.data')
    print(get_str_mapping('Adult.data'))
    print('Mapping for Adult.test')
    print(get_str_mapping('Adult.test'))

if __name__ == '__main__':
    main()