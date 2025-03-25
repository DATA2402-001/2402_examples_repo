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

    return pt

df = pd.read_csv('./pivot_table/sample_data.csv')
print(make_pivot_table(df, 'year', 'dept', 'sales'))
