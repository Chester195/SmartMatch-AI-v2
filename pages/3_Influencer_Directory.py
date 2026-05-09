import streamlit as st
import pandas as pd

st.title("Influencer Directory")
st.subheader("Browse and filter influencers")

# Load dataset
data = pd.read_csv("dataset.csv")

# Unique influencers only
influencers = data[[
    "influencer_id",
    "followers",
    "engagement_rate",
    "niche"
]].drop_duplicates().copy()

# Simple internal score for display
influencers["score"] = (
    influencers["engagement_rate"] * 0.7 +
    (influencers["followers"] / influencers["followers"].max()) * 5 * 0.3
).round(2)

# ----------------------------
# Filters
# ----------------------------
st.sidebar.header("Filter Influencers")

selected_niches = st.sidebar.multiselect(
    "Niche",
    options=sorted(influencers["niche"].unique()),
    default=sorted(influencers["niche"].unique())
)

min_followers = int(influencers["followers"].min())
max_followers = int(influencers["followers"].max())

followers_range = st.sidebar.slider(
    "Followers Range",
    min_value=min_followers,
    max_value=max_followers,
    value=(min_followers, max_followers)
)

min_engagement = float(influencers["engagement_rate"].min())
max_engagement = float(influencers["engagement_rate"].max())

engagement_range = st.sidebar.slider(
    "Engagement Rate Range",
    min_value=min_engagement,
    max_value=max_engagement,
    value=(min_engagement, max_engagement)
)

# ----------------------------
# Apply filters
# ----------------------------
filtered = influencers[
    (influencers["niche"].isin(selected_niches)) &
    (influencers["followers"] >= followers_range[0]) &
    (influencers["followers"] <= followers_range[1]) &
    (influencers["engagement_rate"] >= engagement_range[0]) &
    (influencers["engagement_rate"] <= engagement_range[1])
].copy()

# Sort option
sort_option = st.selectbox(
    "Sort by",
    ["score", "followers", "engagement_rate"]
)

filtered = filtered.sort_values(by=sort_option, ascending=False)

# ----------------------------
# Metrics
# ----------------------------
col1, col2, col3 = st.columns(3)
col1.metric("Visible Influencers", len(filtered))
col2.metric("Avg Followers", f"{int(filtered['followers'].mean()) if len(filtered) > 0 else 0:,}")
col3.metric("Avg Engagement", f"{filtered['engagement_rate'].mean():.2f}" if len(filtered) > 0 else "0.00")

st.markdown("---")

# ----------------------------
# Table
# ----------------------------
st.dataframe(
    filtered[[
        "influencer_id",
        "niche",
        "followers",
        "engagement_rate",
        "score"
    ]],
    use_container_width=True
)