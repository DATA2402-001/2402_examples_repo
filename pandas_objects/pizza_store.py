import pandas as pd

df = pd.DataFrame({
    'customer_name': ['eric', 'alice', 'bob'],
    'pizza_size': [8, 10, 12],
    'qty': [1, 1, 2],
})

prices = {
    8: 9.00, 10: 12.00, 12: 14.00
}

def compute_subtotal(frame: pd.DataFrame) -> pd.DataFrame:
    # step 1: convert pizza size to a price
    for size, price in prices.items():
        frame.loc[frame['pizza_size'] == size, 'subtotal'] = price
    frame['subtotal'] *= frame['qty']
    
    # another way, using replace
    # frame['subtotal'] = frame['pizza_size'].replace(prices)
    
    return frame

def compute_discount(frame: pd.DataFrame) -> pd.DataFrame:
    """compute a 10% discount where name == 'eric' """
    eric_customers = frame['customer_name'] == 'eric'
    frame['discount'] = frame['subtotal'] * 0.1 * eric_customers
    return frame

def compute_gst_total(frame: pd.DataFrame) -> pd.DataFrame:
    frame['gst'] = (frame['subtotal'] - frame['discount']) * 0.05
    frame['total'] = frame['subtotal'] - frame['discount'] + frame['gst']
    return frame

df = compute_subtotal(df)
df = compute_discount(df)
df = compute_gst_total(df)
print(df)