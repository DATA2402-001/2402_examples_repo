

def normalize_numeric(data: list[dict]) -> list[dict]:
    """
    Accepts a dataset stored as a list of dictionaries. Normalizes each column of
    numeric values (ignores columns of text values).
    normalized_value = (raw_value - column_min) / (column_max - column_min)
    :param data: the dataset, as a list of dictionaries - one dictionary per row
    :return: the transformed dataset, with all numeric columns normalized 
    """
    for column in data[0].keys():

        # check if this is a numeric column by looking at the first row
        if type(data[0][column]) != float:
            continue

        # identify max and min values in this column
        this_column = [row[column] for row in data]
        max_value = max(this_column)
        min_value = min(this_column)
        
        # normalized_value = (raw_value - column_min) / (column_max - column_min)
        for row in data:
            row[column] = (row[column] - min_value) / (max_value - min_value)
    
    return data


def fill_missing_values(data: list[dict]) -> list[dict]:
    """
    Accepts a dataset stored as a list of dictionaries. Fills all missing
    values with the mode (most common value) of the column.
    For this assignment, only text columns will have missing values.
    :param data: the dataset, as a list of dictionaries - one dictionary per row
    :return: the transformed dataset, with all missing values filled. 
    """
    
    # psuedocode of how to do this
    # for each column:
    #   check if a text column - if not, skip
    #   find the most common value
    #   replace all missing ('') with that most common value

    for column in data[0].keys():

        # check if this is a numeric column by looking at the first row
        if type(data[0][column]) != str:
            continue

        # find the most common value in this column
        value_counts = dict()
        for row in data:
            value = row[column]
            if value != '':
                # add the value to our dict if it's not there, or bump the count up
                if value in value_counts:
                    value_counts[value] += 1
                else:
                    value_counts[value] = 1

                # here's a more concise way to write the above
                #value_counts[value] = value_counts.get(value, 0) + 1

        # identify the most common value
        biggest_count = 0
        mode_value = ''
        for string, count in value_counts.items():
            if count > biggest_count:
                biggest_count = count
                mode_value = string
        
        # replace all missing values
        for row in data:
            if row[column] == '':
                row[column] = mode_value
    
    return data
