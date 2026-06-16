import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

csv_path = os.path.join(
    BASE_DIR,
    "data",
    "jan to may police violation_anonymized791b166.csv"
)

df = pd.read_csv(csv_path)

# Remove No Junction
df = df[df["junction_name"] != "No Junction"]

# Count violations per junction
junction_stats = (
    df.groupby("junction_name")
      .agg(
          violations=("junction_name", "count"),
          violation_types=("violation_type", "nunique")
      )
      .reset_index()
)

# Normalize
scaler = MinMaxScaler()

junction_stats["violations_norm"] = scaler.fit_transform(
    junction_stats[["violations"]]
)

junction_stats["types_norm"] = scaler.fit_transform(
    junction_stats[["violation_types"]]
)

# Parking Impact Score
junction_stats["PIS"] = (
    0.8 * junction_stats["violations_norm"] +
    0.2 * junction_stats["types_norm"]
) * 100

# Risk Classification
def classify(score):
    if score >= 75:
        return "Critical"
    elif score >= 50:
        return "High"
    elif score >= 25:
        return "Moderate"
    else:
        return "Low"

junction_stats["Risk"] = junction_stats["PIS"].apply(classify)

# Top 20
top_pis = (
    junction_stats
    .sort_values("PIS", ascending=False)
    .head(20)
)

print(top_pis[
    ["junction_name", "violations", "PIS", "Risk"]
])

output_path = os.path.join(
    BASE_DIR,
    "outputs",
    "parking_impact_scores.csv"
)

top_pis.to_csv(output_path, index=False)

print("\nSaved:", output_path)