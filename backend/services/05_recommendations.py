import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

pis_path = os.path.join(
    BASE_DIR,
    "outputs",
    "parking_impact_scores.csv"
)

df = pd.read_csv(pis_path)

recommendations = []

for _, row in df.iterrows():

    risk = row["Risk"]
    junction = row["junction_name"]

    if risk == "Critical":
        action = (
            f"Deploy towing units immediately at {junction}. "
            f"Increase patrol frequency and temporary barricading."
        )

    elif risk == "High":
        action = (
            f"Increase enforcement presence at {junction} "
            f"during peak periods."
        )

    elif risk == "Moderate":
        action = (
            f"Monitor {junction} and conduct periodic patrols."
        )

    else:
        action = (
            f"Routine observation is sufficient at {junction}."
        )

    recommendations.append(action)

df["Recommendation"] = recommendations

print(
    df[
        [
            "junction_name",
            "Risk",
            "Recommendation"
        ]
    ].head(10)
)

output_path = os.path.join(
    BASE_DIR,
    "outputs",
    "recommendations.csv"
)

df.to_csv(output_path, index=False)

print("\nSaved:", output_path)