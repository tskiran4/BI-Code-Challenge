from src.ingestion import ingest_broker_data
from src.normalize import normalize_data
from src.aggregate import aggregate_data
from src.reporting import calculate_summary_stats, filter_by_broker, display_policy

def main():

    #Ingestion
    broker_1_df = ingest_broker_data("data/broker1.csv" , "broker_1")
    broker_2_df = ingest_broker_data("data/broker2.csv" , "broker_2")

    if broker_1_df is None or broker_2_df is None:
        print("Error: Could not load data from one or both brokers.")
        return
    
    # Aggregating Data
    aggregated_df = aggregate_data(broker_1_df , broker_2_df)

    # Normalizing Data 
    normalized_df = normalize_data(aggregated_df)

    # Interface
    while True:
        print("\nInsurance Data Aggregation Tool")
        print("1. Display Summary Statistics")
        print("2. Filter by Broker")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            summary_stats = calculate_summary_stats(normalized_df)
            print("\nSummary Statistics :")
            print("---------------------------------------")
            print(f"  Total Number of Policies: {summary_stats['total_policies']}")
            print(f"  Total Active Policies: {summary_stats['active_policies']}")
            print(f"  Total Customers: {summary_stats['total_customers']}")
            print(f"  Total Insured Amount (Active): ${summary_stats['total_insured_amount']:.2f}")
            print(f"  Average Policy Duration (Days): {summary_stats['avg_policy_duration']:.0f}")
            print("---------------------------------------")

        elif choice == '2':
            broker_name = input("Enter broker name (broker_1 or broker_2): ")
            if broker_name not in ["broker_1", "broker_2"]:
                print("\nInvalid Broker Name")
                continue
            filtered_policies = filter_by_broker(normalized_df , broker_name)
            for index, policy in filtered_policies.iterrows():
                    display_policy(policy)

        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
