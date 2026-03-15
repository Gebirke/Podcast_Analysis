import re
import pandas as pd
import os
from pathlib import Path


def load_generated_episodes(folder_path="generated_episodes"):
    """
    Load all files from the generated_episodes folder.
    
    Args:
        folder_path (str): Path to the generated_episodes folder
        
    Returns:
        dict: Dictionary containing loaded files
    """
    loaded_files = {}
    
    # Check if folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' not found")
        return loaded_files
    
    # Get all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue
        
        try:
            # Load based on file extension
            if filename.endswith('.csv'):
                loaded_files[filename] = pd.read_csv(file_path)
                print(f"Loaded CSV: {filename}")
            elif filename.endswith('.json'):
                loaded_files[filename] = pd.read_json(file_path)
                print(f"Loaded JSON: {filename}")
            elif filename.endswith(('.xlsx', '.xls')):
                loaded_files[filename] = pd.read_excel(file_path)
                print(f"Loaded Excel: {filename}")
            elif filename.endswith('.txt'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    loaded_files[filename] = f.read()
                print(f"Loaded TXT: {filename}")
        except Exception as e:
            print(f"Error loading {filename}: {str(e)}")
    
    return loaded_files


# Example usage:
if __name__ == '__main__':
    episodes_data = load_generated_episodes("generated_episodes")
    
    # Access individual files
    for filename, data in episodes_data.items():
        print(f"
{filename}:")
        if isinstance(data, pd.DataFrame):
            print(data.head())
        else:
            print(f"Type: {type(data)}")

