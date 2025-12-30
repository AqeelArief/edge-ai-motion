import pandas as pd

# Load the windowed data (from Phase 2)
windowed_df = pd.read_csv("windowed_data.csv")  # You can create this from Phase 2 code

# Define a simple threshold for anomaly
# Any window with unusually high acceleration is flagged
threshold = 1.0  # tweak if needed

# Flag anomalies
windowed_df['alert'] = ((windowed_df['mean_x'] > threshold) |
                        (windowed_df['mean_y'] > threshold) |
                        (windowed_df['mean_z'] > threshold) |
                        (windowed_df['max_x'] > threshold) |
                        (windowed_df['max_y'] > threshold) |
                        (windowed_df['max_z'] > threshold))

# Show flagged windows
alerts = windowed_df[windowed_df['alert']]
print("Flagged Windows (possible anomalies):")
print(alerts)
