import streamlit as st
import pandas as pd

st.set_page_config(page_title="Automated Sales BI Dashboard", layout="wide")

st.title("📊 Automated Sales BI Dashboard")
st.caption("Prototype ready for Snowflake live data integration & Cortex Code automation")

@st.cache_data
def load_sample_data():
    data = {
        "Month": ["2026-06", "2026-06", "2026-07", "2026-07", "2026-08", "2026-08", "2026-09", "2026-09"],
        "Region": ["EMEA", "North America", "EMEA", "North America", "EMEA", "North America", "EMEA", "North America"],
        "Product": ["Enterprise Plan", "Pro Plan", "Enterprise Plan", "Pro Plan", "Pro Plan", "Enterprise Plan", "Enterprise Plan", "Pro Plan"],
        "Revenue":,
        "Deals_Closed": [14, 22, 16, 25, 28, 18, 19, 30]
    }
    return pd.DataFrame(data)

df = load_sample_data()

# Filtry w panelu bocznym
st.sidebar.header("Filter Metrics")
selected_regions = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)
selected_products = st.sidebar.multiselect(
    "Select Product",
    options=df["Product"].unique(),
    default=df["Product"].unique()
)

filtered_df = df[
    (df["Region"].isin(selected_regions)) &
    (df["Product"].isin(selected_products))
]

# Główne wskaźniki KPI
col1, col2, col3 = st.columns(3)
total_rev = filtered_df["Revenue"].sum()
total_deals = filtered_df["Deals_Closed"].sum()
avg_deal = total_rev / total_deals if total_deals > 0 else 0

col1.metric("Total Revenue", f"${total_rev:,.0f}", "+12.4%")
col2.metric("Closed Deals", f"{total_deals}", "+8")
col3.metric("Avg. Deal Size", f"${avg_deal:,.0f}", "+3.1%")

st.divider()

# Wykresy i tabela
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Monthly Revenue Trend")
    monthly_rev = filtered_df.groupby("Month")["Revenue"].sum()
    st.line_chart(monthly_rev)

with chart_col2:
    st.subheader("Revenue by Region")
    region_rev = filtered_df.groupby("Region")["Revenue"].sum()
    st.bar_chart(region_rev)

st.subheader("Detailed Sales Records")
st.dataframe(filtered_df, use_container_width=True)
