import pandas as pd

# Load dataset
df = pd.read_csv("/Users/omraj/ParkPulseAI/data/jan to may police violation_anonymized791b166.csv")

# Display total records
print("Total Records:", len(df))

# Top parking violations
print("\nTop Parking Violations:")
print(df["violation_type"].value_counts().head(10))

# Top junctions
print("\nTop Junctions:")
print(df["junction_name"].value_counts().head(10))

# Top police stations
print("\nTop Police Stations:")
print(df["police_station"].value_counts().head(10))