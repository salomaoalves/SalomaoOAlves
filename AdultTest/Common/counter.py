
# Counter Functions
def read():
    with open("counter.txt", "r") as file_pointer:
        file_content = file_pointer.read()
    return int(file_content)

def write(idx_data):
    with open("counter.txt", "w") as file_pointer:
        file_pointer.write(str(idx_data))