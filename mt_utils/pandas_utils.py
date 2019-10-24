import numpy as np
import pandas as pd


def clean_col_names_after_groupby(df: pd.DataFrame) -> pd.DataFrame:
    """creates column names by flattening names from hierarchical index"""
    column_names = [
        "_".join(col).strip() if len(col[1]) > 0 else col[0]
        for col in df.columns.values
    ]
    return column_names
