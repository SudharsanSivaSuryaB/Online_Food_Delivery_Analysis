# 🍽️ Online Food Delivery Analysis: Data-Driven Business Insights

 📌 Project Overview
This project focuses on analyzing online food delivery data to uncover meaningful business insights related to customer behavior, order patterns, delivery performance, restaurant efficiency, and revenue trends.  
The project uses real-world, noisy data and applies data cleaning, exploratory data analysis (EDA), feature engineering, SQL integration, and interactive dashboard visualization.

The final outcome supports data-driven decision-making for food delivery platforms.



 🎯 Objectives
- Analyze customer ordering behavior
- Identify top-spending customers and high-demand periods
- Evaluate delivery performance and operational inefficiencies
- Assess restaurant and cuisine-level performance
- Track revenue, profit, and cancellation trends
- Build an interactive dashboard for KPI monitoring



 🛠️ Technologies Used
- Python
- Pandas & NumPy
- SQL (MySQL)
- SQLAlchemy
- Power BI / Streamlit
- Matplotlib, Seaborn, Plotly
- Git & GitHub



 📂 Dataset
- Source: Online Food Delivery Dataset
- Records: ~100,000 orders
- Features: 25 columns including:
  - Customer details
  - Order information
  - Restaurant attributes
  - Delivery performance
  - Financial metrics



 🔄 Project Workflow

# 1️⃣ Data Collection
- Load raw online food delivery dataset.

# 2️⃣ Data Cleaning & Preprocessing
- Handle missing values (mean, median, mode)
- Remove or cap outliers (delivery time, order value)
- Correct invalid data (ratings > 5, negative profits)
- Standardize categorical values
- Ensure logical consistency

# 3️⃣ Exploratory Data Analysis (EDA)
- Order value and delivery time distributions
- City-wise and cuisine-wise demand
- Weekend vs weekday order trends
- Distance vs delivery delay analysis
- Cancellation reason analysis
- Correlation between numeric features

# 4️⃣ Feature Engineering
- Order Day Type (Weekday / Weekend)
- Peak Hour Indicator
- Profit Margin %
- Delivery Performance Category
- Customer Age Groups

# 5️⃣ Database Integration
- Store cleaned data in MySQL
- Create normalized tables
- Insert data using SQLAlchemy
- Enable scalable querying

# 6️⃣ Dashboard Development
- Interactive dashboard using Power BI or Streamlit
- Real-time KPI tracking and filters



 📊 Key Analytics Performed

# Customer & Order Analysis
- Identify top-spending customers
- Age group vs order value analysis
- Weekend vs weekday demand patterns

# Revenue & Profit Analysis
- Monthly revenue trends
- Discount impact on profit
- High-revenue cities and cuisines

# Delivery Performance
- Average delivery time by city
- Distance vs delivery delay
- Delivery rating vs delivery time

# Restaurant Performance
- Top-rated restaurants
- Cancellation rate by restaurant
- Cuisine-wise performance comparison

# Operational Insights
- Peak hour demand analysis
- Payment mode preferences
- Cancellation reason analysis



 📈 Dashboard KPIs
- Total Orders
- Total Revenue
- Average Order Value
- Average Delivery Time
- Cancellation Rate
- Average Delivery Rating
- Profit Margin %



 ⚙️ Installation & Setup

# Install Dependencies

pip install -r requirements.txt



# Run Data Cleaning

   python data_cleaning.py


# Import Data into MySQL

   python data_import_sql.py

# Run Streamlit Dashboard

   python -m streamlit run dashboard/app.py


Author

Sudharsan Siva Surya

Data Analyst / Software Developer
