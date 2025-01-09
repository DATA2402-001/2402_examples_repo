def validate_table(table: list[list]):
    """
    table is supposed to have a fixed number of columns.
    so every row should have the same number of elements.
    raise Exception if it doesn't
    """
    n_columns = len(table[0])
    for i in range(len(table)):
        row = table[i]
        if len(row) != n_columns:
            raise Exception(f"first row had {n_columns} elements, row index {i} has {len(row)}")


my_table = [
    ['Alice', 12345, 4.0],
    ['Bob', 98765, 3.7],
    ['Charles', 54555, 2.8],
    ['Denise', 11111]
]
validate_table(my_table)