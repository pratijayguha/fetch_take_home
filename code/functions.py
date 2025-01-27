# <TODO>: Add Docs

import io
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def standardize_datetime(df: pd.DataFrame, col_name: str, format: str):
    return pd.to_datetime(df[col_name], format=format, errors="coerce")