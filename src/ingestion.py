import pandas as pd

# Read CSV and append broker name
def ingest_broker_data(file_path, broker_name):
    try:
        broker_df = pd.read_csv(file_path)
        broker_df['Broker'] = broker_name
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None 
    except Exception as e:
        print(f"Error reading CSV file {file_path}: {e}")
        return None
    return broker_df