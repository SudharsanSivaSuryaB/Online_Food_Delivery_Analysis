# ONLINE FOOD DELIVERY DATA ANALYSIS & CLEANING

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD DATA

FILE_PATH = "data/ONINE_FOOD_DELIVERY_ANALYSIS.csv"

df = pd.read_csv(FILE_PATH)

print("\nDataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())





#  DATA CLEANING & PREPROCESSING

# Customer Age Column Data Cleaning

# Check missing values
print("Missing Age Values:", df['Customer_Age'].isnull().sum())

# Check missing percentage
missing_percent = df['Customer_Age'].isnull().mean() * 100
print("Missing %:", missing_percent)

# Fill missing values with median and save back to df
median_age = df['Customer_Age'].median()
df['Customer_Age'] = df['Customer_Age'].fillna(median_age)
# alternatively: df['Customer_Age'].fillna(median_age, inplace=True)

# Verify
print("Missing Age Values After Treatment:", df['Customer_Age'].isnull().sum())
print("Median Age Used:", median_age)

print(df.head())


# Customer Gender Column Data Cleaning

# Check missing
print("Missing Gender:", df['Customer_Gender'].isnull().sum())

# Check missing percentage
missing_percent = df['Customer_Gender'].isnull().mean() * 100
print("Missing %:", missing_percent)

# Fill with Unknown
df['Customer_Gender'] = df['Customer_Gender'].fillna("Unknown")

# Verify
print("Missing After Treatment for Customer Gender:", df['Customer_Gender'].isnull().sum())
print(df['Customer_Gender'].value_counts().to_string())



# City Column Data Cleaning

# Check missing
print("Missing City:", df['City'].isnull().sum())

# Check missing percentage
missing_percent = df['City'].isnull().mean() * 100
print("Missing %:", missing_percent)

# Fill missing with 'Unknown'
df['City'] = df['City'].fillna("Unknown")

# Verify
print("Missing after treatment for City:", df['City'].isnull().sum())
print(df['City'].value_counts().to_string())





# Area Column Data Cleaning

# Check missing
print("Missing Area:", df['Area'].isnull().sum())

# Check missing percentage
missing_percent = df['Area'].isnull().mean() * 100
print("Missing %:", missing_percent)

# Fill missing with 'Unknown'
df['Area'] = df['Area'].fillna("Unknown")
# Verify
print("Missing after treatment for Area:", df['Area'].isnull().sum())
print(df['Area'].value_counts().to_string())





# Cuisine_Type Column Data Cleaning

# Check missing
print("Missing Cuisine_Type:", df['Cuisine_Type'].isnull().sum())

# Check missing percentage
missing_percent = df['Cuisine_Type'].isnull().mean() * 100
print("Missing %:", missing_percent)

# Fill missing with 'Unknown'
df['Cuisine_Type'] = df['Cuisine_Type'].fillna("Unknown")
# Verify
print("Missing after treatment for Cuisine_Type:", df['Cuisine_Type'].isnull().sum())
print(df['Cuisine_Type'].value_counts().to_string())



# Order_Date Column Data Cleaning


# Check missing
print("Missing Order_Date:", df['Order_Date'].isnull().sum())
print("Missing Order_Date %:",df['Order_Date'].isnull().mean() * 100)

# Drop rows where Order_Date is missing
df = df.dropna(subset=['Order_Date'])

# Verify
print("Missing after treatment:", df['Order_Date'].isnull().sum())
print("New dataset shape:", df.shape)



# Order_Time Column Data Cleaning


# Check missing
print("Missing Order_Time:", df['Order_Time'].isnull().sum())
print("Missing Order_Time %:",df['Order_Time'].isnull().mean() * 100)

# Drop rows where Order_Time is missing
df = df.dropna(subset=['Order_Time'])

# Verify
print("Missing after treatment:", df['Order_Time'].isnull().sum())
print("New dataset shape:", df.shape)



# Delivery_Time_Min Column Data Cleaning

# Check missing
print("Missing Delivery_Time_Min:", df['Delivery_Time_Min'].isnull().sum())
print("Missing Delivery_Time_Min %:",df['Delivery_Time_Min'].isnull().mean() * 100)

# Step 1: Fill using City median
df['Delivery_Time_Min'] = df.groupby('City')['Delivery_Time_Min'] \
                             .transform(lambda x: x.fillna(x.median()))

# Step 2: Fill any remaining missing with overall median
df['Delivery_Time_Min'] = df['Delivery_Time_Min'].fillna(df['Delivery_Time_Min'].median())

# Verify
print("Missing after treatment for Delivery_Time_Min:", df['Delivery_Time_Min'].isnull().sum())
print("Final Median:", df['Delivery_Time_Min'].median())
print(
    df.groupby('City')['Delivery_Time_Min']
      .median().to_string()
)



# Distance_km Column Data Cleaning

# Check missing
print("Missing Distance_km:", df['Distance_km'].isnull().sum())
print("Missing Distance_km %:",df['Distance_km'].isnull().mean() * 100)

# Step 1: Fill using City median
df['Distance_km'] = df.groupby('City')['Distance_km'] \
                             .transform(lambda x: x.fillna(x.median()))

# Step 2: Fill any remaining missing with overall median
df['Distance_km'] = df['Distance_km'].fillna(df['Distance_km'].median())
# Verify
print("Missing after treatment for Distance_km:", df['Distance_km'].isnull().sum())
print("Final Median:", df['Distance_km'].median())
print(
    df.groupby('City')['Distance_km']
      .median().to_string()
)





# Order_Value Column Data Cleaning

# Check missing
print("Missing Order_Value:", df['Order_Value'].isnull().sum())
print("Missing Order_Value %:",df['Order_Value'].isnull().mean() * 100)

# Step 1: Fill using City median
df['Order_Value'] = df.groupby('City')['Order_Value'] \
                             .transform(lambda x: x.fillna(x.median()))

# Step 2: Fill any remaining missing with overall median
df['Order_Value'] = df['Order_Value'].fillna(df['Order_Value'].median())


# Verify
print("Missing after treatment for Order_Value:", df['Order_Value'].isnull().sum())
print("Final Median:", df['Order_Value'].median())
print(
    df.groupby('City')['Order_Value']
      .median().to_string()
)



# Discount_Applied Column Data Cleaning


# Check missing
print("Missing Discount_Applied:", df['Discount_Applied'].isnull().sum())

# Check missing percentage
missing_percent = df['Discount_Applied'].isnull().mean() * 100
print("Missing %:", missing_percent)

# Fill missing with 0 (No discount applied)
df['Discount_Applied'] = df['Discount_Applied'].fillna(0)

# Verify
print("Missing after treatment for Discount_Applied:", df['Discount_Applied'].isnull().sum())

print(df['Discount_Applied'].value_counts().to_string())




# Final_Amount Column Data Cleaning

# Check missing
print("Missing Final_Amount:", df['Final_Amount'].isnull().sum())
print("Missing Final_Amount %:", df['Final_Amount'].isnull().mean() * 100)


# Step 1: Fill only missing Final_Amount using calculation
df.loc[df['Final_Amount'].isnull(), 'Final_Amount'] = (
    df['Order_Value'] - df['Discount_Applied']
)


# Step 2: If still any missing (due to base columns), fill safely
df['Final_Amount'] = df['Final_Amount'].fillna(
    df['Order_Value'] - df['Discount_Applied']
)


# Step 3: Ensure no negative values
df['Final_Amount'] = df['Final_Amount'].clip(lower=0)


# Verify
print("Missing after treatment for Final_Amount:", df['Final_Amount'].isnull().sum())
print("Final Median:", df['Final_Amount'].median())

print(
    df.groupby('City')['Final_Amount']
      .median().to_string()
)


# Payment_Mode Column Data Cleaning

# Check missing
print("Missing Payment_Mode:", df['Payment_Mode'].isnull().sum())
print("Missing Payment_Mode %:", df['Payment_Mode'].isnull().mean() * 100)

# Fill missing with 'Unknown'
df['Payment_Mode'] = df['Payment_Mode'].fillna("Unknown")

# Verify
print("Missing after treatment for Payment_Mode:", df['Payment_Mode'].isnull().sum())
print(df['Payment_Mode'].value_counts().to_string())



# Cancellation_Reason Column Data Cleaning

# 1️ Filter only Cancelled orders
df_cancelled = df[df['Order_Status'] == "Cancelled"]

# 2️ Check total cancelled orders
total_cancelled = len(df_cancelled)
print("Total Cancelled Orders:", total_cancelled)

# 3️ Check missing Cancellation_Reason in Cancelled orders
missing_count = df_cancelled['Cancellation_Reason'].isnull().sum()

# Correct percentage calculation
missing_percent = (missing_count / total_cancelled) * 100

print("Missing Cancellation_Reason (Count):", missing_count)
print("Missing Cancellation_Reason (%):", missing_percent)

# Fill missing reason only for Cancelled orders
df.loc[
    (df['Order_Status'] == "Cancelled") &
    (df['Cancellation_Reason'].isnull()),
    'Cancellation_Reason'
] = "Not Specified"

# Fill Delivered orders with "Not Applicable"
df.loc[
    df['Order_Status'] == "Delivered",
    'Cancellation_Reason'
] = "Not Applicable for Delivered"

# Final Verification

print("\nMissing after treatment for Cancellation_Reason:",
      df['Cancellation_Reason'].isnull().sum())

print("\nUpdated Cancellation Reason Distribution:\n")
print(df['Cancellation_Reason'].value_counts().to_string())







# Delivery_Rating Column Data Cleaning


# Check missing
print("Missing Delivery_Rating:", df['Delivery_Rating'].isnull().sum())
print("Missing Delivery_Rating %:",df['Delivery_Rating'].isnull().mean() * 100)

#  Calculate Median from Delivered Only

median_rating = df.loc[
    df['Order_Status'] == "Delivered",
    'Delivery_Rating'
].median()

print("Median Rating (Delivered Only):", median_rating)


#  Fill Missing for Delivered Orders

df.loc[
    (df['Order_Status'] == "Delivered") &
    (df['Delivery_Rating'].isnull()),
    'Delivery_Rating'
] = median_rating


#  Fill Cancelled Orders with 0

df.loc[
    df['Order_Status'] == "Cancelled",
    'Delivery_Rating'
] = 0


#  Final Verification

print("\nMissing After Treatment:",
      df['Delivery_Rating'].isnull().sum())

print("Final Median Rating:",
      df['Delivery_Rating'].median())

print("\nFinal Distribution:")
print(df['Delivery_Rating'].value_counts().sort_index().to_string())




# Peak_Hour Column Data Cleaning

# Check missing
print("Missing Peak_Hour:", df['Peak_Hour'].isnull().sum())
print("Missing Peak_Hour %:", df['Peak_Hour'].isnull().mean() * 100)

# Find mode
mode_value = df['Peak_Hour'].mode()[0]
print("Mode Value:", mode_value)

# Fill missing and explicitly convert to boolean
df['Peak_Hour'] = df['Peak_Hour'].fillna(mode_value).astype(bool)

# Verify
print("Missing After Treatment:", df['Peak_Hour'].isnull().sum())
print(df['Peak_Hour'].value_counts().to_string())






#  FEATURE ENGINEERING

# ensure date/time columns are datetimes
df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
df['Order_Time'] = pd.to_datetime(df['Order_Time'], format='%H:%M', errors='coerce')

# 5.1 order day type (weekday / weekend)
df['Day_Type'] = np.where(df['Order_Date'].dt.weekday >= 5, 'Weekend', 'Weekday')

# 5.2 peak‑hour indicator (lunch 12‑14, dinner 19‑21)
df['Order_Hour'] = df['Order_Time'].dt.hour
df['Peak_Hour'] = np.where(
    ((df['Order_Hour'].between(12, 14)) |
     (df['Order_Hour'].between(19, 21))),
    True,
    False
)

# 5.3 profit margin percentage
# (assumes Profit_Margin and Order_Value exist in the dataset)
df['Profit_Margin_Pct'] = (df['Profit_Margin'] / df['Order_Value']) * 100

# 5.4 delivery performance category
df['Delivery_Performance'] = pd.cut(
    df['Delivery_Time_Min'],
    bins=[-1, 30, 45, np.inf],
    labels=['Fast', 'On-Time', 'Delayed']
)

# 5.5 customer age groups
df['Age_Group'] = pd.cut(
    df['Customer_Age'],
    bins=[0, 25, 40, 60, np.inf],
    labels=['Youth', 'Adult', 'Middle-Aged', 'Senior']
)


#  SAVE CLEANED DATA
OUTPUT_FILE = "cleaned_data/online_food_delivery_cleaned.csv"   # or any path/name you prefer
df.to_csv(OUTPUT_FILE, index=False)

print("\n Data cleaning complete")
print(f" Cleaned file saved as: {OUTPUT_FILE}")


