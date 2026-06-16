import pandas as pd
import folium
from folium.plugins import HeatMap
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

csv_path = os.path.join(
    BASE_DIR,
    "data",
    "jan to may police violation_anonymized791b166.csv"
)

df = pd.read_csv(csv_path)

# Remove missing coordinates
df = df.dropna(subset=["latitude", "longitude"])

# Bengaluru center
m = folium.Map(
    location=[12.9716, 77.5946],
    zoom_start=12
)

heat_data = df[["latitude", "longitude"]].values.tolist()

HeatMap(heat_data).add_to(m)

output_path = os.path.join(
    BASE_DIR,
    "outputs",
    "parking_heatmap.html"
)

m.save(output_path)

print("Heatmap saved to:")
print(output_path)