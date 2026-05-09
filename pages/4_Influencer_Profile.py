import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

st.title("Influencer Profile")
st.subheader("View individual influencer details and campaign fit")

# ----------------------------
# Check campaign
# ----------------------------
if "campaign" not in st.session_state or not st.session_state.campaign:
    st.warning("Please create a campaign first in the Brand Campaign page.")
    st.stop()

campaign = st.session_state.campaign

# ----------------------------
# Load data
# ----------------------------
data = pd.read_csv("dataset.csv")

# Unique influencers
influencers = data[[
    "influencer_id",
    "followers",
    "engagement_rate",
    "niche"
]].drop_duplicates().copy()

# ----------------------------
# Train model
# ----------------------------
X = data[[
    "followers",
    "engagement_rate",
    "niche",
    "campaign_category",
    "campaign_goal",
    "budget_range",
    "match_score"
]]

y = data["engagement_result"]

X = pd.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# ----------------------------
# Select influencer
# ----------------------------
selected_id = st.selectbox(
    "Select Influencer",
    sorted(influencers["influencer_id"].unique())
)

profile = influencers[influencers["influencer_id"] == selected_id].iloc[0]

# ----------------------------
# Prepare prediction for current campaign
# ----------------------------
profile_input = pd.DataFrame([{
    "followers": profile["followers"],
    "engagement_rate": profile["engagement_rate"],
    "niche": profile["niche"],
    "campaign_category": campaign["category"],
    "campaign_goal": campaign["goal"],
    "budget_range": campaign["budget"],
    "match_score": 0.9 if profile["niche"] == campaign["category"] else 0.4
}])

profile_features = pd.get_dummies(profile_input)
profile_features = profile_features.reindex(columns=X_train.columns, fill_value=0)

predicted_engagement = model.predict(profile_features)[0]

# ----------------------------
# Profile info
# ----------------------------
st.header(f"Profile: {selected_id}")

col1, col2, col3 = st.columns(3)
col1.metric("Niche", profile["niche"])
col2.metric("Followers", f"{int(profile['followers']):,}")
col3.metric("Engagement Rate", f"{profile['engagement_rate']:.2f}")

st.markdown("---")

# ----------------------------
# Campaign fit
# ----------------------------
st.header("Campaign Fit")

col4, col5 = st.columns(2)
col4.metric("Predicted Engagement", f"{predicted_engagement:.2f}")
col5.metric("Match Score", "0.90" if profile["niche"] == campaign["category"] else "0.40")

st.write(
    f"Current campaign: **{campaign['name']}** | "
    f"Category: **{campaign['category']}** | "
    f"Goal: **{campaign['goal']}** | "
    f"Budget: **{campaign['budget']}**"
)

# ----------------------------
# Why this influencer?
# ----------------------------
st.header("Why This Influencer?")

reasons = []

if profile["niche"] == campaign["category"]:
    reasons.append("Strong category alignment with the campaign.")

if profile["engagement_rate"] > 4.5:
    reasons.append("High engagement rate suggests strong audience interaction.")

if profile["followers"] > 50000:
    reasons.append("Large follower base provides stronger audience reach.")

if not reasons:
    reasons.append("This influencer has moderate compatibility with the current campaign.")

for reason in reasons:
    st.write(f"- {reason}")

st.markdown("---")

# ----------------------------
# Simple recommendation summary
# ----------------------------
st.header("Recommendation Summary")

if predicted_engagement >= 6:
    st.success("This influencer is a strong candidate for the current campaign.")
elif predicted_engagement >= 4.5:
    st.info("This influencer is a moderate candidate for the current campaign.")
else:
    st.warning("This influencer may be a weaker fit for the current campaign.")
    