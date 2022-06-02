
# Counter Functions
def read(base):
    with open("counter.txt", "r") as file_pointer:
        file_content = file_pointer.read()
    if base=='Adult.data':
        return int(file_content.split('\n')[0]) #first row
    elif base=='Adult.test':
        return int(file_content.split('\n')[1]) #second row

def write(idx_data, idx_test):
    with open("counter.txt", "w") as file_pointer:
        file_pointer.write(str(idx_data)+'\n'+str(idx_test)) #both rows
