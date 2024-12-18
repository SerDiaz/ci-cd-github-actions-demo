import pandas as pd

def title_dataframe(
    df: pd.DataFrame, 
    columns: list[str]
) -> pd.DataFrame:
    """
    Converts the specified columns of a DataFrame to title case.
    
    Args:
        df (pd.DataFrame): The DataFrame to transform.
        columns (list[str]): List of column names to convert to title case.

    Returns:
        pd.DataFrame: The transformed DataFrame with specified columns in title case.
    """
    for col in columns:
        if col in df.columns:
            df[col] = df[col].str.title()
    return df

def generate_unique_id(
    df: pd.DataFrame, 
    id_col: str, 
    prefix: str = "", 
    overwrite: bool = True
) -> pd.DataFrame:
    """
    Generates a unique ID for each row in the DataFrame.
    
    Args:
        df (pd.DataFrame): The DataFrame to transform.
        id (str): The name of the column to store the generated IDs.
        prefix (str, optional): A prefix for the IDs. Defaults to "id_".
        overwrite (bool, optional): If True, overwrites the column if it already exists.
                                    If False, appends "_new" to the column name. Defaults to True.

    Returns:
        pd.DataFrame: The transformed DataFrame with the generated IDs.
    """
    original_id_col = id_col
    if id_col in df.columns:
        if overwrite:
            df.drop(columns=[id_col], inplace=True)
        else:
            counter = 1
            while id_col in df.columns:
                id_col = f"{original_id_col}_{counter}"
                counter += 1

    df[id_col] = [f"{prefix}{i}" for i in range(1, len(df) + 1)]
    return df



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

def delete_columns(
    df: pd.DataFrame, 
    columns: list[str]
) -> pd.DataFrame:
    """
    Deletes the specified columns from a DataFrame.
    
    Args:
        df (pd.DataFrame): The DataFrame to transform.
        columns (list[str]): List of column names to delete.

    Returns:
        pd.DataFrame: The transformed DataFrame without the specified columns.
    """
    return df.drop(columns=columns, inplace=False)

def move_column_to_front(
    df: pd.DataFrame, 
    column_name: str
) -> pd.DataFrame:
    """
    Moves the specified column to the first position in the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to modify.
        column_name (str): The name of the column to move to the front.

    Returns:
        pd.DataFrame: The modified DataFrame with the specified column as the first one.
    """
    if column_name in df.columns:
        # Reorder columns: put the target column first, then the rest
        cols = [column_name] + [col for col in df.columns if col != column_name]
        return df[cols]
    else:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
