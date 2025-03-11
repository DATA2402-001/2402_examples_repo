import pandas as pd

frame = pd.DataFrame({"b": [4, 7, -3, 2], "a": [0, 1, 0, 1]})

# sort by column b
frame = frame.sort_values("b", inplace=True) # setting inplace=True modifies the original frame, instead of copying

# sort by column a, then b. Do it in descending order
frame = frame.sort_values(['a', 'b'], ascending=False, inplace=True)

print(frame)
