import pandas as pd

# Load your small CSV
data = pd.read_csv("motion_data.csv")

window_size = 3  # number of rows per window
windows = []

for start in range(0, len(data), window_size):
    end = start + window_size
    window = data.iloc[start:end]
    # Calculate simple statistics for this window
    stats = {
        'start_time': window['time'].iloc[0],
        'mean_x': window['acc_x'].mean(),
        'mean_y': window['acc_y'].mean(),
        'mean_z': window['acc_z'].mean(),
        'max_x': window['acc_x'].max(),
        'max_y': window['acc_y'].max(),
        'max_z': window['acc_z'].max(),
    }
    windows.append(stats)

windowed_df = pd.DataFrame(windows)
print(windowed_df)
