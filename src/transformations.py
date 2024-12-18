import pandas as pd

def combine_name_and_surname(
    df: pd.DataFrame, 
    name_col: str, 
    surname_col: str, 
    new_col: str
) -> pd.DataFrame:
    """
    Combines 'name' and 'surname' columns into a single column.
    
    Args:
        df (pd.DataFrame): The DataFrame to transform.
        name_col (str): The column name for 'name'.
        surname_col (str): The column name for 'surname'.
        new_col (str): The name of the new combined column.

    Returns:
        pd.DataFrame: The transformed DataFrame with the new combined column.
    """
    df[new_col] = df[name_col] + " " + df[surname_col]
    return df
