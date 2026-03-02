import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. load cleaned data
df = pd.read_csv("cleaned_data/online_food_delivery_cleaned.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Order_Time"] = pd.to_datetime(df["Order_Time"], format="%H:%M", errors="coerce")

# 2. distribution of order values and delivery time
plt.figure()
sns.histplot(df["Order_Value"], bins=30, kde=True)
plt.title("Order‑value distribution")
plt.tight_layout()
plt.show()

plt.figure()
sns.histplot(df["Delivery_Time_Min"], bins=30, kde=True)
plt.title("Delivery‑time distribution")
plt.tight_layout()
plt.show()

# 3. city‑ and cuisine‑wise order counts
print(df["City"].value_counts().head().to_string())
print(df["Cuisine_Type"].value_counts().head().to_string())

# 4. weekend vs weekday demand
df["Day_Type"] = np.where(df["Order_Date"].dt.weekday >= 5, "Weekend", "Weekday")
df["Day_Type"].value_counts().plot.bar(title="Weekend vs weekday orders")
plt.show()

# 5. distance vs delivery delay
plt.figure()
sns.scatterplot(x="Distance_km", y="Delivery_Time_Min", data=df, alpha=.5)
plt.title("Distance vs delivery time")
plt.tight_layout()
plt.show()

# 6. cancellation reasons
cancelled = df[df["Order_Status"] == "Cancelled"]
print(cancelled["Cancellation_Reason"].value_counts().to_string())

# 7. correlation among numeric features
num_cols = df.select_dtypes(include="number").columns
plt.figure(figsize=(8,6))
sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation matrix")
plt.tight_layout()
plt.show()