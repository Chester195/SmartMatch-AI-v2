import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

st.title("Model Insights")
st.subheader("Machine Learning performance and evaluation")

# ----------------------------
# Load data
# ----------------------------
data = pd.read_csv("dataset.csv")

# ----------------------------
# Prepare data
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

# ----------------------------
# Train model
# ----------------------------
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

baseline_pred = X_test["followers"] / 10000
baseline_mae = mean_absolute_error(y_test, baseline_pred)

# ----------------------------
# Metrics Display
# ----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("MAE", f"{mae:.3f}")
col2.metric("RMSE", f"{rmse:.3f}")
col3.metric("Baseline MAE", f"{baseline_mae:.3f}")

st.markdown("---")

# ----------------------------
# Comparison chart
# ----------------------------
st.header("Performance Comparison")

comparison_df = pd.DataFrame({
    "Metric": ["Model MAE", "Baseline MAE"],
    "Value": [mae, baseline_mae]
})

st.bar_chart(comparison_df.set_index("Metric"))

# ----------------------------
# Explanation
# ----------------------------
st.header("What These Metrics Mean")

st.write(
    "**MAE (Mean Absolute Error)** measures the average prediction error of the model. "
    "Lower values indicate better prediction accuracy."
)

st.write(
    "**RMSE (Root Mean Squared Error)** penalizes larger errors more strongly. "
    "It is useful for understanding whether the model makes large mistakes."
)

st.write(
    "**Baseline MAE** represents a simple traditional method based only on follower count. "
    "Comparing the model against this baseline shows whether AI provides added value."
)

st.markdown("---")

# ----------------------------
# Model overview
# ----------------------------
st.header("Model Overview")

st.write(
    "This prototype uses a **Random Forest Regressor** to predict influencer engagement "
    "for a campaign. The model uses structured features such as follower count, "
    "engagement rate, niche, campaign category, campaign goal, budget range, and match score."
)

st.write(
    "Categorical variables were transformed using **one-hot encoding**, and the dataset "
    "was split into **training and testing sets** before model evaluation."
)

# ----------------------------
# Interpretation
# ----------------------------
st.header("Interpretation")

if mae < baseline_mae:
    st.success(
        "The AI model performs better than the follower-based baseline, suggesting that "
        "machine learning improves influencer selection decisions."
    )
else:
    st.warning(
        "The follower-based baseline performs similarly or better than the AI model in this case."
    )