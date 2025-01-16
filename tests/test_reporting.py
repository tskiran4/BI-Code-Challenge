import pandas as pd
import pytest

from src.reporting import is_policy_active, calculate_summary_stats

 # Sample data for testing
data = {
    "Coverage Amount": [116000.0, 234000.0, 212000.0, 113000.0],
    "Start Date": ["2024-12-16", "2022-11-16", "2024-12-31", "2024-10-17"], 
    "End Date": ["2026-02-14", "2023-03-05", "2025-03-01", "2025-12-16"],
    "Consumer ID": ["Ref1", "Ref2", "Ref3", "Ref4"]
}

# Fixtures
@pytest.fixture
def sample_df():
    return pd.DataFrame(data).copy(deep=True)


@pytest.fixture
def sample_empty_df():
    columns = ["Consumer ID", "Start Date", "End Date", "Coverage Amount", "Broker"]
    return pd.DataFrame(columns=columns)


# Test Cases
def test_is_policy_active():
    """Test the is_policy_active function with various scenarios."""
    today = pd.Timestamp('today').date()  # Convert today to datetime.date

    # Active policy
    assert is_policy_active(
        (pd.Timestamp('today') - pd.DateOffset(days=30)).date(),
        (pd.Timestamp('today') + pd.DateOffset(days=30)).date()
    ) == True

    # Inactive policy - ends today
    assert is_policy_active(
        (pd.Timestamp('today') - pd.DateOffset(days=30)).date(),
        today
    ) == False

    # Inactive policy - starts in the future
    assert is_policy_active(
        (pd.Timestamp('today') + pd.DateOffset(days=30)).date(),
        (pd.Timestamp('today') + pd.DateOffset(days=60)).date()
    ) == False

    # Inactive policy - ended in the past
    assert is_policy_active(
        (pd.Timestamp('today') - pd.DateOffset(days=60)).date(),
        (pd.Timestamp('today') - pd.DateOffset(days=30)).date()
    ) == False

    # Edge case - starts today, ends tomorrow (active)
    assert is_policy_active(
        today,
        (pd.Timestamp('today') + pd.DateOffset(days=1)).date()
    ) == True

    # Null dates
    assert is_policy_active(None, pd.Timestamp("2025-03-01").date()) == False  
    assert is_policy_active(pd.Timestamp("2025-03-01").date(), None) == False 
    assert is_policy_active(None, None) == False
    print("\nPolicy Active Check Test")

# Test summary stats
def test_calculate_summary_stats(sample_df):
   
    # Replicating Normalization Manually
    sample_df['Start Date'] = pd.to_datetime(sample_df['Start Date']).dt.date
    sample_df['End Date'] = pd.to_datetime(sample_df['End Date']).dt.date
    sample_df['Active'] = sample_df.apply(lambda row: is_policy_active(row['Start Date'], row['End Date']), axis=1)
    result = calculate_summary_stats(sample_df)

    assert result["total_policies"] == 4
    assert result["total_customers"] == 4
    assert result["active_policies"] == 3
    assert result["total_insured_amount"] == 441000.0
    assert result["avg_policy_duration"] == 303

# Test Empty policy details 
def test_no_policies(sample_empty_df):
    result = calculate_summary_stats(sample_empty_df)

    # Validate the results
    assert result["total_policies"] == 0
    assert result["total_customers"] == 0
    assert result["active_policies"] == 0
    assert result["total_insured_amount"] == 0
    assert result["avg_policy_duration"] == 0
