from fastapi import APIRouter
import pandas as pd
import os

router = APIRouter()

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")


# ==========================
# HOTSPOTS
# ==========================
@router.get("/hotspots")
def get_hotspots():
    path = os.path.join(
        OUTPUT_DIR,
        "top_hotspots.csv"
    )

    df = pd.read_csv(path)

    return df.to_dict(
        orient="records"
    )


# ==========================
# PARKING IMPACT SCORES
# ==========================
@router.get("/pis")
def get_pis():
    path = os.path.join(
        OUTPUT_DIR,
        "parking_impact_scores.csv"
    )

    df = pd.read_csv(path)

    return df.to_dict(
        orient="records"
    )


# ==========================
# RECOMMENDATIONS
# ==========================
@router.get("/recommendations")
def get_recommendations():
    path = os.path.join(
        OUTPUT_DIR,
        "recommendations.csv"
    )

    df = pd.read_csv(path)

    return df.to_dict(
        orient="records"
    )


# ==========================
# TRAFFIC METRICS
# ==========================
@router.get("/traffic-metrics")
def get_traffic_metrics():

    metrics_path = os.path.join(
        OUTPUT_DIR,
        "traffic_metrics.txt"
    )

    metrics = {
        "queue_length": 0,
        "avg_speed": 0,
        "delay_index": 0,
    }

    if os.path.exists(metrics_path):

        with open(metrics_path, "r") as f:

            lines = f.readlines()

        for line in lines:

            if "Average Queue Length" in line:

                metrics["queue_length"] = float(
                    line.split(":")[1]
                    .strip()
                )

            elif "Average Speed" in line:

                value = (
                    line.split(":")[1]
                    .replace("px/sec", "")
                    .strip()
                )

                metrics["avg_speed"] = float(
                    value
                )

            elif "Delay Index" in line:

                value = (
                    line.split(":")[1]
                    .replace("%", "")
                    .strip()
                )

                metrics["delay_index"] = float(
                    value
                )

    return metrics