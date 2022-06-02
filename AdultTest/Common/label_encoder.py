from sklearn.preprocessing import LabelEncoder
from Common import constants

# Label Encoder function
def label_encode(df, col_name, dict_map):
    le = LabelEncoder().fit(dict_map[col_name])
    return le.transform(df[col_name])

# Convert dataframe types - for all encode_col
def convert_types(data):
    dict_types = {
        "workclass": 'category',
        "education": 'category',
        "marital-status": 'category',
        "occupation": 'category',
        "relationship ": 'category',
        "race": 'category',
        "sex": 'category',
        "native-country": 'category',
        "class": 'category'
    }
    return data.astype(dict_types)

# Transform execution
def transform(data, dict_map):
    error = None

    # do the label encoder for each col
    for col in constants.encode_col:
        try:
            data[col] = label_encode(data,col,dict_map)
        except ValueError as e:
            print(f'In column {col} there is a new value, please add it to the mapping.')
            print(f'Erro message: "{e}"')

    data = convert_types(data)
    return data, error