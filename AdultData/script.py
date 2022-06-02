import warnings
warnings.filterwarnings("ignore")

import time
from Common import constants, sqlite, label_encoder as le, counter, load_data as load

def main():

    data, last_idx = load.extract_data()
    dict_map = constants.dict_map
    data, error = le.transform(data,dict_map)

    #will check the label encoder error
    if error==None:

        #only load dataframe with data
        if data.shape[0]>0:
            print('Loading in SQLite - Adult db')
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
    print('Pipeline Adult.data!')
    
    start_time = time.time()
    n_data, current_idx = main()
    counter.write(current_idx)
    finish_time = time.time()

    time_waist = finish_time - start_time
    print(f'Total time: {time_waist} - runned {n_data/time_waist} rows per second.')
    #sqlite.read('select * from Adult')