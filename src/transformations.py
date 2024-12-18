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

def add_id_to_sales(
    sales_df: pd.DataFrame, 
    sellers_df: pd.DataFrame, 
    sales_col: str, 
    sellers_col: str, 
    id_col: str
) -> pd.DataFrame:
    """
    Adds a seller ID to the sales DataFrame based on a match with the sellers DataFrame.
    
    Args:
        sales_df (pd.DataFrame): The sales DataFrame.
        sellers_df (pd.DataFrame): The sellers DataFrame.
        sales_col (str): The seller column in the sales DataFrame.
        sellers_col (str): The seller column in the sellers DataFrame.
        id_col (str): The ID column in the sellers DataFrame.

    Returns:
        pd.DataFrame: The sales DataFrame with the seller IDs added.
    """
    sales_df = sales_df.merge(
        sellers_df[[sellers_col, id_col]],
        left_on=sales_col,
        right_on=sellers_col,
        how="left"
    )
    return sales_df