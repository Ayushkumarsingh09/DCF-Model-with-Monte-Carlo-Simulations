import json
import pandas as pd

def load_csv(file_path):
    """
    Load a CSV file into a Pandas DataFrame.
    """
    return pd.read_csv(file_path)

def load_json(file_path):
    """
    Load a JSON file.
    """
    with open(file_path, 'r') as f:
        return json.load(f)
