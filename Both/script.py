import warnings
warnings.filterwarnings("ignore")

import time
from Common import constants, sqlite, label_encoder as le, counter, load_data as load


# Get dict label encoder values for mapping
def get_dict_mapping(base):
    if base=='Adult.data':
        dict_map = constants.dict_map_data
    elif base=='Adult.test':
        dict_map = constants.dict_map_test
    return dict_map


def main(base):

    data, last_idx = load.extract_data(base)
    dict_map = get_dict_mapping(base)
    data, error = le.transform(data,dict_map)

    #will check the label encoder error
    if error==None:

        #only load dataframe with data
        if data.shape[0]>0:
            print(f'Loading in SQLite - Adult db - base {base}')
            sqlite.load(data)

            #the last row - to set the last_idx correctly
            if data.shape[0]<constants.row_to_map:
                print('End of the file!!!')
                last_idx = (last_idx-constants.row_to_map) + data.shape[0]

        #when is empty, do nothing - don't change the last_idx
        else:
            print('File empty - nothing more to add!!!')
            last_idx -= constants.row_to_map

    else:
        print('Not able to ingest, Label Encoder Error!!!')
        last_idx -= constants.row_to_map

    return data.shape[0], last_idx


if __name__ == '__main__':
    print('Pipeline Both!')
    
    start_time = time.time()
    n_data, current_idx_data = main('Adult.data')
    n_test, current_idx_test = main('Adult.test')
    counter.write(current_idx_data, current_idx_test)
    finish_time = time.time()

    time_waist = finish_time - start_time
    print(f'Total time: {time_waist} - runned {n_data+n_test/time_waist} rows per second.')
    #sqlite.read('select * from Adult')