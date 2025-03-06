import pandas as pd
import numpy as np

frame = pd.DataFrame(np.random.standard_normal((4, 3)),
                     columns=list("bde"),
                     index=["Utah", "Ohio", "Texas", "Oregon"])
print(frame)
print(frame.sum())
print(frame.sum(axis=1))
print(frame.sum(axis=0))