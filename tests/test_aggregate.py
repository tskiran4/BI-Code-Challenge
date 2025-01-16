import pandas as pd
import pytest

from src.aggregate import aggregate_data

# Sample data for testing
data1 = {
    "PolicyNumber": ["P1", "P2", "P3", None],
    "InsuredAmount": [1000.0, 2000.0, 0, 'invalid'],
    "StartDate": ["01-01-2023", "02/02/2023", "15/06/2024", ""],
    "EndDate": ["01-01-2024", "02/02/2025", "15/06/2025", " "],
    "AdminFee": [10.0, 20.0, 'abc', ""],
    "BusinessDescription": ["Desc1", "Desc2", "Desc3", "Unknown"],
    "BusinessEvent": ["Event1", "Event2", "Event3", "Unknown"],
    "ClientType": ["Type1", "Type2", "Type3", "Unknown"],
    "ClientRef": ["Ref1", "Ref2", "Ref3", "Unknown"],
    "Commission": [50.0, 100.0, 0.0, " "],
    "EffectiveDate": ["01-01-2023", "02/02/2023", "15/06/2024", " "],
    "InsurerPolicyNumber": ["IP1", "IP2", "IP3", "Unknown"],
    "IPTAmount": [5.0, 10.0, 2, ""],
    "Premium": [500.0, 1000.0, 'test', ""],
    "PolicyFee": [20.0, 40.0, 15, None],
    "PolicyType": ["TypeA", "TypeB", "TypeC", "Unknown"],
    "Insurer": ["Insurer1", "Insurer2", "Insurer3", "Unknown"],
    "RenewalDate": ["01-01-2025", "02/02/2026", "15/06/2027", ""],
    "RootPolicyRef": ["Root1", "Root2", "Root3", "Unknown"],
    "Product": ["Product1", "Product2", "Product3", "Unknown"]
}

data2 = {
    "PolicyRef": ["P4", "P5"],
    "CoverageAmount": [3000.0, "4000"],
    "InitiationDate": ["2023-03-01", "2023-04-02"],
    "ExpirationDate": ["2024-03-01", "2025-04-02"],
    "AdminCharges": [15.0, "25"],
    "CompanyDescription": ["Desc4", "Desc5"],
    "ContractEvent": ["Event4", "Event5"],
    "Consumer Category": ["Type4", "Type5"],
    "Consumer ID": ["Ref4", "Ref5"],
    "Broker Fee": [75.0, "125"],
    "Activation Date": ["2023-03-01", "2023-04-02"],
    "Insurance Company Ref": ["IP4", "IP5"],
    "TaxAmount": [7.5, "12.5"],
    "CoverageCost": [750.0, "1250"],
    "ContractFee": [30.0, "50"],
    "ContractCategory": ["TypeD", "TypeE"],
    "Underwriter": ["Insurer4", "Insurer5"],
    "NextRenewalDate": ["2025-03-01", "2026-04-02"],
    "Primary Policy Ref": ["Root4", "Root5"],
    "InsurancePlan": ["Product4", "Product5"]
}


# Fixtures
@pytest.fixture
def sample_df1():
    return pd.DataFrame(data1).copy(deep=True)


@pytest.fixture
def sample_df2():
    return pd.DataFrame(data2).copy(deep=True)


# Test Cases

# Test if columns are correctly renamed
def test_column_renaming(sample_df1, sample_df2):
    combined_df = aggregate_data(sample_df1.copy(), sample_df2.copy())
    expected_columns = [
        "Policy Reference", "Coverage Amount", "Start Date", "End Date",
        "Admin Charges", "Company Description", "Contract Event",
        "Consumer Category", "Consumer ID", "Broker Fee",
        "Activation Date", "Insurance Company Ref", "Tax Amount",
        "Coverage Cost", "Contract Fee", "Contract Category",
        "Underwriter", "NextRenewalDate", "Primary Policy Ref", "Insurance Plan"

    ]
    assert all(col in combined_df.columns for col in expected_columns)
    print("\nColumn Rename Test")
    
# Test Aggregation
def test_data_concatenation(sample_df1, sample_df2):
    """Test if data from both DataFrames is concatenated correctly."""
    combined_df = aggregate_data(sample_df1.copy(), sample_df2.copy())
    assert len(combined_df) == len(sample_df1) + len(sample_df2)
    print("\nConcatenation Test")




