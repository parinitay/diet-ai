import streamlit as st
from generate_diet import generate_diet

st.set_page_config(page_title="AI Diet Generator", page_icon="🥗")

st.title("🥗 AI Diet Recommender")

# User Inputs
gender = st.selectbox("Select Gender", ["Male", "Female"])
age = st.slider("Select Age", 10, 80, 25)
body_comp = st.selectbox("Body Composition", ["Lean", "Average", "Overweight", "Obese"])
activity = st.selectbox("Activity Level", ["Sedentary", "Light", "Moderate", "Active", "Athlete"])

# Generate Button
if st.button("Generate Diet Plan"):
    with st.spinner("🧠 Generating your personalized diet plan..."):
        try:
            diet = generate_diet(
                age=age,
                gender=gender,
                body_comp=body_comp,
                activity_level=activity
            )

            st.subheader("📄 Your AI-Powered Diet Plan")
            for line in diet.split("\n"):
                if line.strip():
                    st.markdown(f"- {line}")

            st.download_button("📥 Download Plan", data=diet, file_name="diet_plan.txt")

        except Exception as e:
            st.error("Something went wrong while generating your diet plan.")
            st.code(str(e))


