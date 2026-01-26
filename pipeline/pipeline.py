import sys

import pandas as pd

print("arguments", sys.argv)
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
day = int(sys.argv[1])

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")

print(df.head())
print(f"Running pipeline for day {day}")

