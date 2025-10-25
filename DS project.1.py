import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset (you can replace this with real data from NCRB or MoRTH reports)
data = {
    'State': ['Tamil Nadu', 'Maharashtra', 'Uttar Pradesh', 'Delhi', 'Karnataka', 'Gujarat'],
    'Total_Accidents': [57000, 48000, 52000, 24000, 41000, 39000],
    'Public_Transport_Accidents': [5000, 4200, 3800, 2000, 3100, 2700],
    'Private_Vehicle_Accidents': [52000, 43000, 47000, 21000, 37000, 35000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display dataset
print("Road Accident Statistics in India (Sample Data):")
print(df)

# Plot 1: Bar chart of total accidents by state
plt.figure(figsize=(10,6))
plt.bar(df['State'], df['Total_Accidents'], color='tomato')
plt.title('Total Road Accidents by State (India)')
plt.xlabel('State')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=30)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Plot 2: Comparison of Public vs Private Transport Accidents
plt.figure(figsize=(10,6))
plt.bar(df['State'], df['Public_Transport_Accidents'], label='Public Transport', color='skyblue')
plt.bar(df['State'], df['Private_Vehicle_Accidents'], bottom=df['Public_Transport_Accidents'], label='Private Vehicles', color='orange')
plt.title('Public vs Private Transport Accidents')
plt.xlabel('State')
plt.ylabel('Number of Accidents')
plt.legend()
plt.xticks(rotation=30)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Plot 3: Pie chart for accident contribution by each state
plt.figure(figsize=(8,8))
plt.pie(df['Total_Accidents'], labels=df['State'], autopct='%1.1f%%', startangle=140)
plt.title('Share of Road Accidents by State')
plt.show()

# Insight: Correlation between public transport and total accidents
correlation = df['Public_Transport_Accidents'].corr(df['Total_Accidents'])
print(f"\nCorrelation between Public Transport and Total Accidents: {correlation:.2f}")