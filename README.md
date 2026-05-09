# SmartMatch AI

SmartMatch AI is an AI-powered platform designed to improve influencer selection for marketing campaigns.

## Overview

In traditional influencer marketing, brands often select influencers based on follower count. This approach is not reliable because a large audience does not always guarantee strong engagement.

This project introduces a data-driven approach using machine learning to predict influencer performance and recommend better candidates for campaigns.

---

## Features

- Campaign creation (category, goal, budget, audience)
- AI-based influencer recommendations
- Comparison with follower-based ranking
- Niche-based influencer filtering
- Influencer directory with filters
- Individual influencer profiles
- Model performance insights

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn (Random Forest Regressor)
- Streamlit

---

## How It Works

1. The user creates a campaign.
2. The system evaluates influencers using a machine learning model.
3. The model predicts expected engagement.
4. Influencers are ranked based on predicted performance.
5. Results are compared against traditional follower-based selection.

---

## Project Structure
prototype_v2/
│
├── Home.py
├── dataset.csv
├── README.md
├── requirements.txt
└── pages/
├── 1_Brand_Campaign.py
├── 2_AI_Recommendations.py
├── 3_Influencer_Directory.py
├── 4_Influencer_Profile.py
└── 5_Model_Insights.py

---

## Model

The system uses a Random Forest Regressor to predict engagement based on influencer and campaign features.

### Input Features
- followers
- engagement_rate
- niche
- campaign_category
- campaign_goal
- budget_range
- match_score

### Target
- engagement_result

---

## Evaluation

The model is evaluated using:
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

It is also compared against a baseline based on follower count, and the AI model shows significantly better performance.

---

## Limitations

- The dataset is synthetic
- The model is trained on simulated data
- The platform is a prototype, not a full production system

---

## Future Improvements

- Use real-world data
- Improve recommendation logic
- Add database and user accounts
- Expand platform functionality

---

## Author

Christian  
Computer Science Student  
CECS 451 – AI Project