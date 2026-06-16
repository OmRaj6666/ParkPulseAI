from ultralytics import YOLO
import cv2
import os
from collections import defaultdict

# ===============================
# PROJECT PATHS
# ===============================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

VIDEO_PATH = os.path.join(
    BASE_DIR,
    "video",
    "sample_parking.mp4"
)

OUTPUT_PATH = os.path.join(
    BASE_DIR,
    "outputs",
    "annotated_parking_fixed.mp4"
)

EVIDENCE_DIR = os.path.join(
    BASE_DIR,
    "outputs",
    "evidence"
)

os.makedirs(EVIDENCE_DIR, exist_ok=True)

print("Loading video:", VIDEO_PATH)

# ===============================
# LOAD MODEL
# ===============================

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(VIDEO_PATH)

fps = cap.get(cv2.CAP_PROP_FPS)

print("FPS:", fps)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

out = cv2.VideoWriter(
    OUTPUT_PATH,
    fourcc,
    fps,
    (width, height)
)

# ===============================
# TRACKING VARIABLES
# ===============================

vehicle_positions = defaultdict(list)
vehicle_speeds = defaultdict(list)

queue_lengths = []

illegal_ids = set()

THRESHOLD_FRAMES = int(fps * 5)   # 5 seconds

NORMAL_SPEED = 25   # px/sec baseline

frame_number = 0

print("\nStarting Detection...\n")

# ===============================
# PROCESS VIDEO
# ===============================

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame_number += 1

    results = model.track(
        frame,
        persist=True,
        classes=[2, 3, 5, 7],  # car,bike,bus,truck
        verbose=False
    )

    annotated = results[0].plot()

    boxes = results[0].boxes

    current_queue = 0

    if boxes.id is not None:

        ids = boxes.id.cpu().numpy().astype(int)

        xyxy = boxes.xyxy.cpu().numpy()

        current_queue = len(ids)

        queue_lengths.append(current_queue)

        for track_id, box in zip(ids, xyxy):

            x1, y1, x2, y2 = box

            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)

            vehicle_positions[track_id].append(
                (center_x, center_y)
            )

            # ======================
            # SPEED ESTIMATION
            # ======================

            if len(vehicle_positions[track_id]) >= 2:

                prev = vehicle_positions[track_id][-2]

                pixel_distance = (
                    (center_x - prev[0]) ** 2 +
                    (center_y - prev[1]) ** 2
                ) ** 0.5

                speed = pixel_distance * fps

                vehicle_speeds[track_id].append(speed)

            # ======================
            # ILLEGAL PARKING
            # ======================

            if len(vehicle_positions[track_id]) > THRESHOLD_FRAMES:

                vehicle_positions[track_id].pop(0)

                first = vehicle_positions[track_id][0]

                distance = (
                    (center_x - first[0]) ** 2 +
                    (center_y - first[1]) ** 2
                ) ** 0.5

                if distance < 30:

                    illegal_ids.add(track_id)

                    cv2.putText(
                        annotated,
                        f"ILLEGAL PARKING ID:{track_id}",
                        (center_x, center_y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 0, 255),
                        2
                    )

                    evidence_path = os.path.join(
                        EVIDENCE_DIR,
                        f"vehicle_{track_id}.jpg"
                    )

                    if not os.path.exists(evidence_path):

                        cv2.imwrite(
                            evidence_path,
                            annotated
                        )

    out.write(annotated)

    if frame_number % 50 == 0:

        print("Processed:", frame_number)

# ===============================
# RELEASE
# ===============================

cap.release()
out.release()

# ===============================
# METRICS
# ===============================

avg_queue = (
    sum(queue_lengths) / len(queue_lengths)
    if queue_lengths else 0
)

all_speeds = []

for speeds in vehicle_speeds.values():

    all_speeds.extend(speeds)

avg_speed = (
    sum(all_speeds) / len(all_speeds)
    if all_speeds else 0
)

delay_index = max(
    0,
    (NORMAL_SPEED - avg_speed)
    / NORMAL_SPEED
) * 100

# ===============================
# SAVE METRICS
# ===============================

metrics_path = os.path.join(
    BASE_DIR,
    "outputs",
    "traffic_metrics.txt"
)

with open(metrics_path, "w") as f:

    f.write(
        f"Average Queue Length: {avg_queue:.2f}\n"
    )

    f.write(
        f"Average Speed: {avg_speed:.2f} px/sec\n"
    )

    f.write(
        f"Delay Index: {delay_index:.2f}%\n"
    )

# ===============================
# SUMMARY
# ===============================

print("\n====================")
print("Detection Complete")
print("====================")

print("Processed Frames:", frame_number)

print(
    "Illegal Vehicles:",
    len(illegal_ids)
)

print(
    "Average Queue Length:",
    round(avg_queue, 2)
)

print(
    "Average Speed:",
    round(avg_speed, 2),
    "px/sec"
)

print(
    "Delay Index:",
    round(delay_index, 2),
    "%"
)

print("\nAnnotated Video:")
print(OUTPUT_PATH)

print("\nEvidence Folder:")
print(EVIDENCE_DIR)

print("\nMetrics:")
print(metrics_path)