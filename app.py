import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("Customer_Segments.csv")

# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(page_title="Customer Segmentation", page_icon="🛒", layout="wide")

st.title("🛍️ Customer Segmentation App")

st.markdown("""
Welcome to the **Customer Segmentation Dashboard**!  
Here you can preview the dataset, explore cluster profiles, and predict the cluster for a customer.
""")

# ---------------------------
# Dataset Preview
# ---------------------------
st.header("📂 Dataset Preview")
st.dataframe(df.head())

# ---------------------------
# Cluster Profiling
# ---------------------------
st.header("🔎 Cluster Profiling")
cluster_profile = df.groupby("Cluster").agg({
    "Recency": "mean",
    "Frequency": "mean",
    "Monetary": "mean",
    "CustomerID": "count"
}).rename(columns={"CustomerID": "NumCustomers"})
st.dataframe(cluster_profile)

st.bar_chart(cluster_profile[["Recency", "Frequency", "Monetary"]])

# ---------------------------
# Predict Cluster
# ---------------------------
st.header("🎯 Predict Cluster for a Customer")

customer_id = st.text_input("Enter CustomerID:")

if st.button("Predict Cluster"):
    if customer_id.isdigit():
        customer_id = int(customer_id)
        if customer_id in df["CustomerID"].values:
            row = df.loc[df["CustomerID"] == customer_id]
            cluster = row["Cluster"].values[0]
            segment = row["Segment"].values[0]
            st.success(f"✅ Customer {customer_id} belongs to **Cluster {cluster} ({segment})**")
        else:
            st.warning("⚠️ Customer ID not found in dataset.")
    else:
        st.warning("⚠️ Please enter a valid numeric CustomerID.")
