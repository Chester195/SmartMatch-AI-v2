import streamlit as st

st.title("Create Campaign")
st.subheader("Define your campaign parameters")

# Inicializar estado si no existe
if "campaign" not in st.session_state:
    st.session_state.campaign = {}

# Formulario
with st.form("campaign_form"):
    
    campaign_name = st.text_input("Campaign Name")

    campaign_category = st.selectbox(
        "Campaign Category",
        ["beauty", "fitness", "food", "lifestyle", "tech"]
    )

    campaign_goal = st.selectbox(
        "Campaign Goal",
        ["awareness", "conversion"]
    )

    budget_range = st.selectbox(
        "Budget Range",
        ["low", "medium", "high"]
    )

    target_audience = st.text_input("Target Audience (optional)")

    submitted = st.form_submit_button("Create Campaign")

    if submitted:
        st.session_state.campaign = {
            "name": campaign_name,
            "category": campaign_category,
            "goal": campaign_goal,
            "budget": budget_range,
            "audience": target_audience
        }

        st.success("Campaign created successfully!")

# Mostrar campaña actual
if st.session_state.campaign:
    st.markdown("---")
    st.header("Current Campaign")

    col1, col2, col3 = st.columns(3)

    col1.metric("Category", st.session_state.campaign["category"])
    col2.metric("Goal", st.session_state.campaign["goal"])
    col3.metric("Budget", st.session_state.campaign["budget"])

    st.write(f"Audience: {st.session_state.campaign['audience']}")