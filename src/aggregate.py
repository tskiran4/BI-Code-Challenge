import pandas as pd

 # Combines two DataFrames by renaming mutual columns.
def aggregate_data(broker_1_df , broker_2_df):
  
    # Rename columns for broker_1_df
    broker_1_df.rename(columns={
        "PolicyNumber": "Policy Reference",
        "InsuredAmount": "Coverage Amount",
        "StartDate": "Start Date",
        "EndDate": "End Date",
        "AdminFee": "Admin Charges",
        "BusinessDescription": "Company Description",
        "BusinessEvent": "Contract Event",
        "ClientType": "Consumer Category",
        "ClientRef": "Consumer ID",
        "Commission": "Broker Fee",
        "EffectiveDate": "Activation Date",
        "InsurerPolicyNumber": "Insurance Company Ref",
        "IPTAmount": "Tax Amount",
        "Premium": "Coverage Cost",
        "PolicyFee": "Contract Fee",
        "PolicyType": "Contract Category",
        "Insurer": "Underwriter",
        "RenewalDate": "NextRenewalDate",
        "RootPolicyRef": "Primary Policy Ref",
        "Product": "Insurance Plan"
    }, inplace=True)

    # Rename columns for broker_2_df
    broker_2_df.rename(columns={
        "PolicyRef": "Policy Reference",
        "CoverageAmount": "Coverage Amount",
        "ExpirationDate": "End Date",
        "AdminCharges": "Admin Charges",
        "InitiationDate": "Start Date",
        "CompanyDescription": "Company Description",
        "ContractEvent": "Contract Event",
        "Consumer ID": "Consumer ID",
        "Broker Fee": "Broker Fee",
        "Activation Date": "Activation Date",
        "Consumer Category": "Consumer Category",
        "Insurance Company Ref": "Insurance Company Ref",
        "TaxAmount": "Tax Amount",
        "CoverageCost": "Coverage Cost",
        "ContractFee": "Contract Fee",
        "ContractCategory": "Contract Category",
        "Underwriter": "Underwriter",
        "NextRenewalDate": "NextRenewalDate",
        "Primary Policy Ref": "Primary Policy Ref",
        "InsurancePlan": "Insurance Plan"
    }, inplace=True)

    aggregated_df = pd.concat([broker_1_df , broker_2_df], ignore_index=True)
    
    return aggregated_df
