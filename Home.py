import streamlit as st
import pandas as pd

st.set_page_config(page_title="SmartMatch AI", layout="wide")

# Load dataset
data = pd.read_csv("dataset.csv")

# Basic metrics
total_influencers = data["influencer_id"].nunique()
avg_engagement = data["engagement_rate"].mean()
total_categories = data["niche"].nunique()
avg_followers = int(data["followers"].mean())

# Title and intro
st.title("SmartMatch AI")
st.subheader("AI-Powered Influencer Marketing Platform")

st.write(
    "SmartMatch AI helps brands identify the best influencers for marketing campaigns "
    "by predicting expected engagement and comparing AI-based recommendations against "
    "traditional follower-based selection."
)

# Metrics row
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Influencers", total_influencers)
col2.metric("Avg Engagement Rate", f"{avg_engagement:.2f}")
col3.metric("Categories", total_categories)
col4.metric("Avg Followers", f"{avg_followers:,}")

st.markdown("---")

# How it works
st.header("How It Works")
st.write(
    "Brands create a campaign by selecting campaign parameters such as category, goal, "
    "budget, and target audience. The system then analyzes influencer data, predicts "
    "expected engagement, and ranks influencers based on performance."
)

# Platform sections
st.header("Platform Sections")

section1, section2 = st.columns(2)

with section1:
    st.markdown("### Brand Side")
    st.write("- Create a campaign")
    st.write("- Define category, goal, budget, and audience")
    st.write("- Receive AI-based influencer recommendations")

with section2:
    st.markdown("### Influencer Side")
    st.write("- Browse influencer directory")
    st.write("- View influencer profiles")
    st.write("- Understand why influencers are recommended")

st.markdown("---")

# Quick preview
st.header("What This Prototype Demonstrates")
st.write(
    "This prototype demonstrates how machine learning can improve decision-making in "
    "influencer marketing by prioritizing predicted engagement instead of relying only "
    "on superficial metrics like follower count."
)

st.info("Use the navigation menu on the left to explore the platform.")