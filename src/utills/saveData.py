
def save(fileName: str, data: str):
    with open(fileName, 'a') as file:
    # Append the data to the file
        file.write(data + '\n')