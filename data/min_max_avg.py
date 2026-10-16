import pandas as pd
import numpy as np

df = pd.read_csv("dh_param_est_error.csv")
error_col = df["error"]

avg = np.average(error_col)
min = np.min(error_col)
max = np.max(error_col)

print(f"avg: {avg}, min: {min}, max: {max}")