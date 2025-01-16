import pandas as pd

# Convert numberic values to float
def safe_convert_to_float(value):
   
    if pd.isna(value):
        return 0.0
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0
    
# Normalize numberic values and dates 
def normalize_data(aggregated_df):

    # Normalize numeric fields
    numeric_columns = [ 'Coverage Amount', 'Admin Charges', 'Broker Fee',
                     'Tax Amount', 'Coverage Cost', 'Contract Fee' ]
    
    for col in numeric_columns:
        if col in aggregated_df.columns:
            aggregated_df[col] = aggregated_df[col].apply(safe_convert_to_float)
            
    
    # Ensure consistent data types
    aggregated_df['Start Date'] = pd.to_datetime(aggregated_df['Start Date'], errors='coerce', dayfirst=True).dt.date 
    aggregated_df['End Date'] = pd.to_datetime(aggregated_df['End Date'], errors='coerce', dayfirst=True).dt.date
    aggregated_df['Activation Date'] = pd.to_datetime(aggregated_df['Activation Date'], errors='coerce', dayfirst=True).dt.date  
    

    aggregated_df.fillna("Unknown", inplace=True)

    # Output for manual verification
    aggregated_df.to_csv("data/output/normalized_data.csv", index=False)

    return aggregated_df
