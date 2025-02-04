

def load(filename: str) -> list[dict]:
    """
    A generic function that loads data from a text file. Tries to load the data
    using the load_from_csv and load_from_json functions. If neither of these functions
    works (i.e. the data is not encoded in csv or valid json format) raises an Exception with
    the message, "ERROR - data must be in CSV or valid JSON format"
    :param filename: the file path of the file to read
    :return: the dataset as a list of dictionaries - one dict per row of the file
            each dictionary should map column names to values. Numeric values should be type float.
    """
    try:
        return load_from_csv(filename)
    except:
        print('loading from csv failed')
    
    try:
        return load_from_json(filename)
    except:
        print('loading from json failed')
    
    raise Exception('Error - data must be in JSON or CSV format')


def load_from_csv(filename: str) -> list[dict]:
    """
    reads a dataset in csv format. converts numeric data to float.
    :param filename: the file path of the csv file to read
    :return: the dataset as a list of dictionaries - one dict per row of the file
            each dictionary should map column names to values
    """
    data = []
    with open(filename, 'r') as file:  # also fine to explicitly open and close the file
        
        # read the column names from 1st row
        header = file.readline().strip().split(',')

        # go line-by-line through the rest - could have also read in the whole file, since it's small
        for line in file:
            values = line.split(',')
            this_row = dict()

            # build the dictionary to represent this line
            for i in range(len(values)):

                # try to cast to float - if the value is numeric this will work
                try:
                    values[i] = float(values[i])
                except ValueError:
                    pass
                
                # associate this value with it's column name
                this_row[header[i]] = values[i]

            data.append(this_row)
    
    if len(data) < 1: # this will reject the JSON file
        raise Exception('CSV data empty')
    return data    


def load_from_json(filename: str) -> list[dict]:
    """
    reads a dataset in json format. converts numeric data to float.
    raises an AttributeError if the dictionaries in the json file do not all have the same keys
    :param filename: the file path of the json data to read
    :return: the dataset as a list of dictionaries - one dict per object in the file
            each dictionary should map column names to values
    """    
    data = []
    with open(filename, 'r') as file:
        contents = file.read()
    
    # drop the first set of brackets
    contents = contents[2:-2]

    # split into rows (wherever there's a },{)
    contents = contents.split('},{')

    # parse each of the rows
    for row in contents:
        this_row = dict()
        for key_value_pair in row.split(','):
            key, value = key_value_pair.split(':')
            key = key.strip('"')
            value = value.strip('"')

            # try to cast to float - if the value is numeric this will work
            try:
                value = float(value)
            except ValueError:
                pass

            this_row[key] = value
        data.append(this_row)
    
    # check that all rows have the same keys
    expected_keys = set(data[0])
    for row in data[1:]:
        if set(row) != expected_keys:
            raise Exception('Not all rows have same keys')

    return data



def save_to_csv(data: list[dict], filename: str) -> None:
    """
    saves a dataset to csv format
    :param data: the dataset, as a list of dictionaries - one dictionary per row
    :param filename: the file path where the data should be saved in csv format
    """
    raise NotImplementedError("you need to write this function!")


def save_to_json(data: list[dict], filename: str) -> None:
    """
    saves a dataset to json format
    :param data: the dataset, as a list of dictionaries - one dictionary per row
    :param filename: the file path where the data should be saved in json format
    """
    raise NotImplementedError("you need to write this function!")
