import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
from urllib.parse import quote_plus




if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True




# PAGE CONFIG
st.set_page_config(page_title="Online Food Delivery Dashboard", layout="wide")
st.title("🍔 Online Food Delivery – Analytics Dashboard")

# DATABASE CONNECTION
password = quote_plus("12345")
mysql_url = f"mysql+pymysql://root:{password}@localhost:3306/b115_b118"
engine = create_engine(mysql_url)

@st.cache_data
def load_data():
    return pd.read_sql("SELECT * FROM online_food_delivery_data", engine)

df = load_data()

# SIDEBAR FILTERS

sidebar_transform = "translateX(0)" if st.session_state.sidebar_open else "translateX(-320px)"

st.markdown(
    f"""
    <style>
    section[data-testid="stSidebar"] {{
        transform: {sidebar_transform};
        transition: transform 0.35s ease-in-out;
        z-index: 1001;
    }}

    section[data-testid="stSidebar"] > div {{
        padding-top: 3rem;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.header("🔎 Filters")
cities = st.sidebar.multiselect("City", df["City"].unique(), df["City"].unique())
cuisines = st.sidebar.multiselect("Cuisine", df["Cuisine_Type"].unique(), df["Cuisine_Type"].unique())
day_type = st.sidebar.multiselect("Day Type", df["Day_Type"].unique(), df["Day_Type"].unique())



filtered_df = df[
    (df["City"].isin(cities)) &
    (df["Cuisine_Type"].isin(cuisines)) &
    (df["Day_Type"].isin(day_type))
]

#  DATA DISPLAY

st.header("1️⃣ Data Display")
st.write("Filtered & cleaned dataset from MySQL:")
st.dataframe(filtered_df, use_container_width=True)

#  VISUALIZATIONS (EDA & ANALYTICS)

st.header("2️⃣ Visualizations")


# Customer & Order Analysis

st.subheader("👥 Customer & Order Analysis")

col1, col2 = st.columns(2)

with col1:
    st.write("Top-Spending Customers")
    top_customers = filtered_df.groupby("Customer_ID")["Final_Amount"].sum().nlargest(10)
    st.bar_chart(top_customers)

with col2:
    st.write("Age Group vs Order Value")
    age_order = filtered_df.groupby("Age_Group")["Order_Value"].mean()
    st.bar_chart(age_order)

st.write("Weekend vs Weekday Order Pattern")
weekday_orders = filtered_df["Day_Type"].value_counts()
st.bar_chart(weekday_orders)


# Revenue & Profit Analysis

st.subheader("💰 Revenue & Profit Analysis")

col1, col2 = st.columns(2)

with col1:
    filtered_df["Order_Date"] = pd.to_datetime(filtered_df["Order_Date"])
    monthly_revenue = filtered_df.groupby(filtered_df["Order_Date"].dt.to_period("M"))["Final_Amount"].sum()
    st.line_chart(monthly_revenue)

with col2:
    st.write("Discount Impact on Profit")
    sns.scatterplot(data=filtered_df, x="Discount_Applied", y="Profit_Margin")
    st.pyplot(plt.gcf())
    plt.clf()

st.write("High-Revenue Cities")
city_revenue = filtered_df.groupby("City")["Final_Amount"].sum().sort_values(ascending=False)
st.bar_chart(city_revenue)

st.write("High-Revenue Cuisines")
cuisine_revenue = filtered_df.groupby("Cuisine_Type")["Final_Amount"].sum()
st.bar_chart(cuisine_revenue)


# Delivery Performance

st.subheader("🚚 Delivery Performance")

col1, col2 = st.columns(2)

with col1:
    st.write("Average Delivery Time by City")
    delivery_city = filtered_df.groupby("City")["Delivery_Time_Min"].mean()
    st.bar_chart(delivery_city)

with col2:
    st.write("Distance vs Delivery Time")
    sns.scatterplot(data=filtered_df, x="Distance_km", y="Delivery_Time_Min")
    st.pyplot(plt.gcf())
    plt.clf()

st.write("Delivery Rating vs Delivery Time")
sns.boxplot(data=filtered_df, x="Delivery_Rating", y="Delivery_Time_Min")
st.pyplot(plt.gcf())
plt.clf()


# Restaurant Performance

st.subheader("🏪 Restaurant Performance")

col1, col2 = st.columns(2)

with col1:
    st.write("Top-Rated Restaurants")
    top_rest = filtered_df.groupby("Restaurant_Name")["Restaurant_Rating"].mean().nlargest(10)
    st.bar_chart(top_rest)

with col2:
    st.write("Cancellation Rate by Restaurant")
    cancel_rate = filtered_df[filtered_df["Order_Status"] == "Cancelled"].groupby("Restaurant_Name").size().rename("Cancellation Count")
    st.bar_chart(cancel_rate)

st.write("Cuisine-wise Performance (Revenue)")
st.bar_chart(filtered_df.groupby("Cuisine_Type")["Final_Amount"].sum())


# Operational Insights

st.subheader("⚙ Operational Insights")

col1, col2 = st.columns(2)

with col1:
    st.write("Peak Hour Demand")
    st.bar_chart(filtered_df["Order_Hour"].value_counts().sort_index())

with col2:
    st.write("Payment Mode Preferences")
    st.bar_chart(filtered_df["Payment_Mode"].value_counts())

st.write("Cancellation Reason Analysis")
cancel_reason = filtered_df["Cancellation_Reason"].value_counts()
st.bar_chart(cancel_reason)

#  INSIGHTS & KPIs
st.header("3️⃣ Insights & KPIs")

total_orders = filtered_df.shape[0]
total_revenue = filtered_df["Final_Amount"].sum()
avg_order_value = filtered_df["Order_Value"].mean()
avg_delivery_time = filtered_df["Delivery_Time_Min"].mean()
cancel_rate = (filtered_df["Order_Status"] == "Cancelled").mean() * 100
avg_rating = filtered_df["Delivery_Rating"].mean()
profit_margin = filtered_df["Profit_Margin_Pct"].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("📦 Total Orders", total_orders)
col2.metric("💰 Total Revenue", f"{total_revenue:,.0f}")
col3.metric("🧾 Avg Order Value", f"{avg_order_value:.2f}")
col4.metric("🚚 Avg Delivery Time", f"{avg_delivery_time:.1f} min")

col1, col2, col3 = st.columns(3)
col1.metric("❌ Cancellation Rate", f"{cancel_rate:.2f}%")
col2.metric("⭐ Avg Delivery Rating", f"{avg_rating:.2f}")
col3.metric("📊 Profit Margin %", f"{profit_margin:.2f}%")

st.markdown("""
### 👥 Customers & Orders
- A small group of customers contributes a large portion of total revenue.
- Middle-aged customers generally place higher-value orders.
- Order volume is noticeably higher on weekends than on weekdays.

### 💰 Revenue & Profit
- Revenue fluctuates month by month with a few clear peak periods.
- Higher discounts often lead to lower profit margins.
- A limited number of cities and cuisines generate most of the revenue.

### 🚚 Delivery Performance
- Delivery time varies across different cities.
- Longer delivery distances usually result in longer delivery times.
- Faster deliveries tend to receive better customer ratings.

### 🏪 Restaurant Performance
- Highly rated restaurants attract more customer orders.
- Some restaurants experience higher cancellation rates than others.
- Certain cuisines consistently perform better in terms of revenue and ratings.

### ⚙ Operations
- Let us Assume that Demand should be highest during lunch and dinner peak hours.
- Most customers prefer digital payment methods.
- Delivery delays are the most common reason for order cancellations.

### 📊 Overall Summary
- Revenue is driven by loyal customers and peak-hour demand.
- Delivery speed has a strong impact on customer satisfaction.
- Reducing cancellations can improve both profit and customer ratings.
""")