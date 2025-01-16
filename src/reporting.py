import pandas as pd
from datetime import date

 # Check if policy is active
def is_policy_active(start_date, end_date):

    today = pd.Timestamp('today').date()
  
    if not isinstance(start_date, date) or not isinstance(end_date, date):
        return False

    return start_date <= today and end_date > today

 # Calculates general summary of policies across borkers
def calculate_summary_stats(aggregated_df):
 
    if aggregated_df.empty:
        return {
            "total_policies": 0,
            "total_customers": 0,
            "active_policies": 0,
            "total_insured_amount": 0,
            "avg_policy_duration": 0
        }
    aggregated_df['Active'] = aggregated_df.apply(lambda row: is_policy_active(row['Start Date'], row['End Date']), axis=1)

    total_policies = len(aggregated_df)
    unique_customers = aggregated_df['Consumer ID'].nunique()

    active_policies = aggregated_df[aggregated_df['Active']] 
    active_policies_count = len(active_policies)
    total_insured_amount = active_policies['Coverage Amount'].sum()

    if active_policies_count > 0:
        policy_durations = (pd.to_datetime(active_policies['End Date']) - pd.to_datetime(active_policies['Start Date'])).dt.days
        avg_policy_duration = int(policy_durations.sum() / active_policies_count)
    else:
        avg_policy_duration = 0

    summary_stats = {  # Correctly create the dictionary
        "total_policies": total_policies,
        "total_customers": unique_customers,
        "active_policies": active_policies_count,
        "total_insured_amount": total_insured_amount,
        "avg_policy_duration": avg_policy_duration
    }

    return summary_stats


 # filter
def filter_by_broker(aggregated_df, broker_name):
    filtered_df = aggregated_df[aggregated_df['Broker'] == broker_name]

    if filtered_df.empty:
        error_msg = f"Broker '{broker_name}' not found."
        return error_msg

    return filtered_df

  # Display individual policies in a neat format
def display_policy(policy):
    """
    Displays a single policy in a user-friendly format.
    """
    
    print(f"""
        ----------------------------------------
        Policy Reference:         {policy['Policy Reference']}
        Coverage Amount:          ${policy['Coverage Amount']:.2f}
        Start Date:               {policy['Start Date']}
        End Date:                 {policy['End Date']}
        Admin Charges:            ${policy['Admin Charges']:.2f}
        Company Description:      {policy['Company Description']}
        Contract Event:           {policy['Contract Event']}
        Consumer Category:        {policy['Consumer Category']}
        Consumer ID:               {policy['Consumer ID']}
        Broker Fee:                ${policy['Broker Fee']:.2f}
        Activation Date:          {policy['Activation Date']}
        Insurance Company Ref:      {policy['Insurance Company Ref']}
        Tax Amount:               ${policy['Tax Amount']:.2f}
        Coverage Cost:            ${policy['Coverage Cost']:.2f}
        Contract Fee:             ${policy['Contract Fee']:.2f}
        Contract Category:        {policy['Contract Category']}
        Underwriter:              {policy['Underwriter']}
        Insurance Plan:           {policy['Insurance Plan']}
        NextRenewalDate:          {policy['NextRenewalDate']}
        Primary Policy Ref:         {policy['Primary Policy Ref']}
        Broker:                   {policy['Broker']}
        ----------------------------------------
    """)