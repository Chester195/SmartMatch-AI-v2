# SmartMatch AI — Influencer Recommendation Platform

SmartMatch AI is a machine learning-based application developed as an academic project to explore data-driven influencer selection for marketing campaigns.

The platform uses a **Random Forest Regressor** to predict influencer engagement and generate campaign-specific recommendations based on audience size, engagement rate, niche, and campaign characteristics.

Built with Python and Streamlit, the application provides an interactive interface for creating campaigns, exploring influencer profiles, comparing recommendation strategies, and evaluating model performance.

## Tech Stack

- **Python** — Application logic and machine learning
- **Streamlit** — Interactive web interface
- **Pandas & NumPy** — Data processing and analysis
- **Scikit-learn** — Random Forest regression and model evaluation
- **CSV** — Synthetic dataset storage

## Key Features

- **Campaign Creation:** Define campaign category, marketing goal, budget range, and target audience.
- **AI-Based Recommendations:** Rank influencers according to predicted engagement.
- **Ranking Comparison:** Compare model-based recommendations against follower-count and niche-based rankings.
- **Influencer Directory:** Browse and filter influencers by niche, audience size, and engagement rate.
- **Influencer Profiles:** Explore individual influencer metrics and predicted campaign compatibility.
- **Model Insights:** Evaluate prediction performance using MAE and RMSE.

## How It Works

1. Users create a marketing campaign with their preferred parameters.
2. The application loads a synthetic dataset containing influencer and campaign information.
3. Categorical features are transformed using one-hot encoding.
4. A Random Forest Regressor is trained to predict engagement results.
5. The model generates engagement predictions for influencers based on the selected campaign.
6. Influencers are ranked and displayed alongside alternative selection strategies.

## Machine Learning Model

**Algorithm:** Random Forest Regressor

**Input Features:**
- Follower count
- Engagement rate
- Influencer niche
- Campaign category
- Campaign goal
- Budget range
- Niche match score

**Prediction Target:** Engagement result

The dataset is divided into training (80%) and testing (20%) subsets.

Model performance is evaluated using:
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Comparison against a simple follower-based baseline

## Project Structure

```text
prototype_v2/
├── Home.py
├── dataset.csv
├── requirements.txt
└── pages/
    ├── 1_Brand_Campaign.py
    ├── 2_AI_Recommendations.py
    ├── 3_Influencer_Directory.py
    ├── 4_Influencer_Profile.py
    └── 5_Model_Insights.py
```

## Getting Started

**1. Clone the repository**

```bash
git clone https://github.com/Chester195/SmartMatch-AI-v2.git
cd SmartMatch-AI-v2
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Run the application**

From the directory containing `Home.py`:

```bash
streamlit run Home.py
```

## Limitations

- The project uses synthetic data rather than real marketing campaign results.
- Model predictions are intended for experimentation and educational purposes.
- The recommendation approach has not been validated against real-world campaign outcomes.
- The application is an academic prototype rather than a production-ready platform.

## Project Purpose

SmartMatch AI was developed to explore the application of machine learning to recommendation and ranking problems.

The project provided practical experience with:

- Supervised machine learning
- Feature engineering and categorical encoding
- Regression model training and evaluation
- Data analysis and visualization
- Interactive application development with Streamlit

## Author

**Christian Ojeda**  
Software Engineering Student  
Universidad Autónoma de Guadalajara

GitHub: [@Chester195](https://github.com/Chester195)
