import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv('new_data.csv')

frequency_table = pd.crosstab(df["hotel_name"], df["customer_review"])

target_groups = ["Excellent", "Very Good", "Good", "Poor"]
filtered_table = frequency_table.reindex(columns=target_groups, fill_value=0)
print("--------------------------------------")
print("--Hotel Review Category Frequencies--")
print("-------------------------------------")
print(filtered_table)

filtered_columns = [col for col in target_groups if col in frequency_table.columns]
final_freq_df = frequency_table[filtered_columns]

colors = ["purple", "blue", "orange", "red"]

ax = final_freq_df.plot(kind="bar", figsize=(10,6), edgecolor="black", color=colors)

for container in ax.containers:
    ax.bar_label(container, fmt='%d')
    
plt.title("Hotel Review Category Frequencies")
plt.xlabel("Hotel Name")
plt.ylabel("Categorical Reviews")
plt.xticks(rotation=0, ha='center')
ax.legend(
    title="Review Categories of each Hotel",
    loc="upper center",
    bbox_to_anchor=(0.5, -0.15),
    ncol=4
)

plt.subplots_adjust(bottom=0.25)
plt.tight_layout()
plt.savefig('hotel_frequency_chart.png')
plt.show()