import pandas as pd

# Load raw motion data
data = pd.read_csv("motion_data.csv")

WINDOW_SIZE = 3
ALERT_THRESHOLD = 1.0

alerts = []

for start in range(0, len(data), WINDOW_SIZE):
    window = data.iloc[start:start + WINDOW_SIZE]

    mean_x = window['acc_x'].mean()
    mean_y = window['acc_y'].mean()
    mean_z = window['acc_z'].mean()

    max_x = window['acc_x'].max()
    max_y = window['acc_y'].max()
    max_z = window['acc_z'].max()

    # Decide whether to alert
    is_alert = (
        mean_x > ALERT_THRESHOLD or
        mean_y > ALERT_THRESHOLD or
        mean_z > ALERT_THRESHOLD or
        max_x > ALERT_THRESHOLD or
        max_y > ALERT_THRESHOLD or
        max_z > ALERT_THRESHOLD
    )

    if is_alert:
        alerts.append({
            "start_time": window['time'].iloc[0],
            "mean_x": mean_x,
            "mean_y": mean_y,
            "mean_z": mean_z,
            "max_x": max_x,
            "max_y": max_y,
            "max_z": max_z,
            "reason": "unusual motion detected"
        })

print("Alerts sent from edge device:")
for alert in alerts:
    print(alert)
