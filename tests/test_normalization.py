import pandas as pd
import pytest

from src.normalize import normalize_data, safe_convert_to_float

# Sample data for testing
data = {
    "Policy Reference": ["P1", "P2", "P3", None],
    "Coverage Amount": [1000.0, 2000.0, 0, 'invalid'],
    "Start Date": ["01-01-2023", "02/02/2023", "15/06/2024", ""],
    "End Date": ["01-01-2024", "02/02/2025", "15/06/2025", " "],
    "Admin Charges": [10.0, 20.0, 'abc', ""],
    "Company Description": ["Desc1", "Desc2", "Desc3", "Unknown"],
    "Contract Event": ["Event1", "Event2", "Event3", "Unknown"],
    "Consumer Category": ["Type1", "Type2", "Type3", "Unknown"],
    "Consumer ID": ["Ref1", "Ref2", "Ref3", "Unknown"],
    "Broker Fee": [50.0, 100.0, 0.0, " "],
    "Activation Date": ["01-01-2023", "02/02/2023", "15/06/2024", " "],
    "Insurance Company Ref": ["IP1", "IP2", "IP3", "Unknown"],
    "Tax Amount": [5.0, 10.0, 2, ""],
    "Coverage Cost": [500.0, 1000.0, 'test', ""],
    "Contract Fee": [20.0, 40.0, 15, None],
    "Contract Category": ["TypeA", "TypeB", "TypeC", "Unknown"],
    "Underwriter": ["Insurer1", "Insurer2", "Insurer3", "Unknown"],
    "NextRenewalDate": ["01-01-2025", "02/02/2026", "15/06/2027", ""],
    "Primary Policy Ref": ["Root1", "Root2", "Root3", "Unknown"]
}


# Fixtures
@pytest.fixture
def sample_df():
    return pd.DataFrame(data).copy(deep=True)

# Test Cases

# Test normalization or numeric values
def test_numeric_field_normalization(sample_df):
    combined_df = normalize_data(sample_df.copy())

    assert combined_df["Coverage Amount"].dtype == 'float64'
    assert combined_df["Admin Charges"].dtype == 'float64'
    assert combined_df["Broker Fee"].dtype == 'float64'
    assert combined_df["Tax Amount"].dtype == 'float64'
    assert combined_df["Coverage Cost"].dtype == 'float64'
    assert combined_df["Contract Fee"].dtype == 'float64'

    # Check for specific values after conversion
    assert combined_df.loc[2, "Coverage Amount"] == 0.0  # Originally 0
    assert combined_df.loc[3, "Coverage Amount"] == 0.0  # Originally 'invalid'
    assert combined_df.loc[2, "Admin Charges"] == 0.0  # Originally 'abc'
    assert combined_df.loc[3, "Admin Charges"] == 0.0  # Originally ""

    print("\nNumeric Values Normalization Test")


 # Null Values 
def test_nan_handling(sample_df):
    combined_df = normalize_data(sample_df.copy())

    # Test if originally NaN values are now 'Unknown'
    assert combined_df.loc[3, "Policy Reference"] == "Unknown"
    assert combined_df.loc[3, "Company Description"] == "Unknown"
    print("\nBlank Value Handling Test")


