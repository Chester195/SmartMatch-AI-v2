import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

st.title("AI Recommendations")

# Check if campaign exists
if "campaign" not in st.session_state or not st.session_state.campaign:
    st.warning("Please create a campaign first.")
    st.stop()

campaign = st.session_state.campaign

st.subheader(f"Campaign: {campaign['name']}")
st.write(
    f"**Category:** {campaign['category']} | "
    f"**Goal:** {campaign['goal']} | "
    f"**Budget:** {campaign['budget']} | "
    f"**Audience:** {campaign['audience']}"
)

# ----------------------------
# Load data
# ----------------------------
data = pd.read_csv("dataset.csv")

# ----------------------------
# Prepare model
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
# Prepare influencer predictions
# ----------------------------
influencers = data[[
    "influencer_id",
    "followers",
    "engagement_rate",
    "niche"
]].drop_duplicates()

pred_input = influencers.copy()
pred_input["campaign_category"] = campaign["category"]
pred_input["campaign_goal"] = campaign["goal"]
pred_input["budget_range"] = campaign["budget"]

# Match score
pred_input["match_score"] = pred_input["niche"].apply(
    lambda x: 0.9 if x == campaign["category"] else 0.4
)

# Features for model
pred_features = pred_input[[
    "followers",
    "engagement_rate",
    "niche",
    "campaign_category",
    "campaign_goal",
    "budget_range",
    "match_score"
]]

pred_features = pd.get_dummies(pred_features)
pred_features = pred_features.reindex(columns=X_train.columns, fill_value=0)

# Predict
pred_input["predicted_engagement"] = model.predict(pred_features)

# ----------------------------
# Rankings
# ----------------------------
top_ai = pred_input.sort_values(
    by="predicted_engagement", ascending=False
).head(10).copy()

top_followers = pred_input.sort_values(
    by="followers", ascending=False
).head(10).copy()

top_niche = pred_input[
    pred_input["niche"] == campaign["category"]
].sort_values(
    by="predicted_engagement", ascending=False
).head(10).copy()

# Round display values
top_ai["predicted_engagement"] = top_ai["predicted_engagement"].round(2)
top_followers["predicted_engagement"] = top_followers["predicted_engagement"].round(2)
top_niche["predicted_engagement"] = top_niche["predicted_engagement"].round(2)

# ----------------------------
# Display tables
# ----------------------------
st.header("Top Influencers Recommended by AI")
st.write(
    "These are the highest-performing influencers overall based on predicted engagement, "
    "regardless of niche."
)
st.dataframe(
    top_ai[[
        "influencer_id",
        "followers",
        "engagement_rate",
        "niche",
        "predicted_engagement"
    ]],
    use_container_width=True
)

st.header("Top Influencers by Followers")
st.write(
    "This is the traditional ranking approach based only on audience size."
)
st.dataframe(
    top_followers[[
        "influencer_id",
        "followers",
        "engagement_rate",
        "niche",
        "predicted_engagement"
    ]],
    use_container_width=True
)

st.header("Top Influencers in Campaign Niche")
st.write(
    "This table shows only influencers whose niche matches the campaign category, "
    "ranked by predicted engagement."
)
st.dataframe(
    top_niche[[
        "influencer_id",
        "followers",
        "engagement_rate",
        "niche",
        "predicted_engagement"
    ]],
    use_container_width=True
)

# ----------------------------
# Performance comparison
# ----------------------------
st.header("Performance Comparison")

avg_ai = top_ai["predicted_engagement"].mean()
avg_followers = top_followers["predicted_engagement"].mean()
avg_niche = top_niche["predicted_engagement"].mean() if len(top_niche) > 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("AI Ranking Avg", f"{avg_ai:.2f}")
col2.metric("Followers Ranking Avg", f"{avg_followers:.2f}")
col3.metric("Niche Ranking Avg", f"{avg_niche:.2f}")

comparison_df = pd.DataFrame({
    "Method": ["AI", "Followers", "Niche"],
    "Engagement": [avg_ai, avg_followers, avg_niche]
})

st.bar_chart(comparison_df.set_index("Method"))

if avg_ai > avg_followers:
    st.success("AI-based ranking performs better than follower-based selection.")
else:
    st.warning("Follower-based ranking performs similarly or better.")

# ----------------------------
# Why these influencers?
# ----------------------------
st.header("Why These Influencers?")

example = top_ai.head(3)

for _, row in example.iterrows():
    st.write(f"**{row['influencer_id']}**")

    reasons = []

    if row["niche"] == campaign["category"]:
        reasons.append("Strong category alignment")

    if row["engagement_rate"] > 4.5:
        reasons.append("High engagement rate")

    if row["followers"] > 50000:
        reasons.append("Large audience reach")

    if row["niche"] != campaign["category"]:
        reasons.append("Strong performance despite weaker niche match")

    st.write(", ".join(reasons))
    st.markdown("---")