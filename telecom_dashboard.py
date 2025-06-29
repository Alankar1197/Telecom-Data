import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("telecom_dashboard_data.csv")

# Normalize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

st.title("📊 Telecom Data Dashboard")

# Dataset Preview
st.subheader("📄 Dataset Preview")
st.dataframe(df.head())

# Show available columns
st.write("✅ Available Columns:", df.columns.tolist())

# Key Metrics
score_cols = ['engagement_score', 'experience_score', 'satisfaction_score']
if all(col in df.columns for col in score_cols):
    st.subheader("⭐ Key Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Avg Engagement", round(df['engagement_score'].mean(), 2))
    col2.metric("Avg Experience", round(df['experience_score'].mean(), 2))
    col3.metric("Avg Satisfaction", round(df['satisfaction_score'].mean(), 2))
else:
    st.warning("⚠️ Some key metric columns are missing.")

# Satisfaction Cluster Distribution
if 'satisfaction_cluster' in df.columns:
    st.subheader("📊 Satisfaction Cluster Distribution")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='satisfaction_cluster', palette='Set2', ax=ax)
    st.pyplot(fig)

# Correlation Heatmap
st.subheader("📌 Correlation Heatmap")
num_df = df.select_dtypes(include='number')
if not num_df.empty:
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(num_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    st.pyplot(fig)

#streamlit run telecom_dashboard.py