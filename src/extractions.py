import pandas as pd

def read_json(file_path: str) -> pd.DataFrame:
    """
    Reads a JSON file and converts it into a Pandas DataFrame.
    
    Args:
        file_path (str): The path to the JSON file.

    Returns:
        pd.DataFrame: A DataFrame containing the JSON data.
    """
    return pd.read_json(file_path)

def read_csv(file_path: str) -> pd.DataFrame:
    """
    Reads a CSV file and converts it into a Pandas DataFrame.
    
    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: A DataFrame containing the CSV data.
    """
    return pd.read_csv(file_path)
