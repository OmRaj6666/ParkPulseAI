import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

csv_path = os.path.join(
    BASE_DIR,
    "data",
    "jan to may police violation_anonymized791b166.csv"
)

df = pd.read_csv(csv_path)

# Remove "No Junction"
df = df[df["junction_name"] != "No Junction"]

# Top 20 hotspots
top_hotspots = (
    df.groupby("junction_name")
      .size()
      .reset_index(name="violations")
      .sort_values("violations", ascending=False)
      .head(20)
)

print("\nTOP 20 PARKING HOTSPOTS\n")
print(top_hotspots)

# Save results
output_path = os.path.join(
    BASE_DIR,
    "outputs",
    "top_hotspots.csv"
)

top_hotspots.to_csv(output_path, index=False)

print("\nSaved to:", output_path)