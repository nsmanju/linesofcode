import matplotlib.pyplot as plt
import numpy as np

data = {
    'MS-DOS': 4_000,
    'WhatsApp': 30_000,
    'Telegram': 50_000,
    'Zoom': 60_000,
    'TikTok': 80_000,
    'Shuttle': 400_000,
    'Minecraft': 500_000,
    'Instagram': 1_000_000,
    'Drone': 3_500_000,
    'YouTube': 5_400_000,
    'Warcraft': 5_500_000,
    '787': 6_500_000,
    'Chrome': 6_700_000,
    'Volt': 10_000_000,
    'Twitter': 10_000_000,
    'Android': 12_000_000,
    'iOS': 12_000_000,
    'Firefox': 21_000_000,
    'XP': 45_000_000,
    'Hadron': 50_000_000,
    'Ubuntu': 50_000_000,
    'FB': 62_000_000,
    'MacOS X': 84_000_000,
    'Tesla': 100_000_000,
    'Google': 2_000_000_000
}

# Sort the data by the number of users in descending order
sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)

# Extract the items and the number of users for plotting
items = [item[0] for item in sorted_data]
users = [item[1] for item in sorted_data]

# Generate a color palette for the bars
num_bars = len(items)
color_palette = plt.cm.get_cmap('tab20', num_bars)

# Create the bar plot
#plt.figure(figsize=(12, 8))
plt.figure(figsize=(12, 6))
bars = plt.bar(items, users, color=color_palette(np.arange(num_bars)))

plt.xticks(rotation=45)
plt.xlabel('Application', loc='center')
plt.ylabel('Number of Lines (in millions)')
plt.title('Number of Lines of Code For Different Applications')

# Set the y-axis to use a logarithmic scale
plt.yscale('log')

# Remove the legend with colors from the right-hand side
plt.legend().remove()

plt.tight_layout()

# Display the plot
plt.show()
