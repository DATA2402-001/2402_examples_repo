import pandas as pd

def make_pivot_table(
        frame: pd.DataFrame,
        index: str,
        column: str,
        values: str
) -> pd.DataFrame:
    row_index = frame[index].unique()
    col_index = frame[column].unique()
    pt = pd.DataFrame(
        index = row_index,
        columns = col_index
    )

    for row_value in row_index:
        for col_value in col_index:
            matching_rows = (frame[index] == row_value) & (frame[column] == col_value)
            aggregated_value = frame.loc[matching_rows, values].mean()
            pt.loc[row_value, col_value] = aggregated_value        

    return pt

df = pd.read_csv('./pivot_table/sample_data.csv')
print(make_pivot_table(df, 'year', 'dept', 'sales'))

# get all the same info using a groupby
print(df.groupby(['year', 'dept'])['sales'].mean())
