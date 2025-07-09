import streamlit as st
from crewai_gcp.crew import GotCharacterMatcher
from datetime import datetime

st.set_page_config(page_title="Game of Thrones Character & Dragon Matcher", page_icon="🐉", layout="centered")

st.title("Game of Thrones Character & Dragon Matcher 🏰🐉")
st.markdown("""
Step into the world of Westeros! Answer a few questions and discover which Game of Thrones character and dragon you truly are.
""")

with st.form("got_form"):
    user_name = st.text_input("What's your name?", "")
    user_age = st.number_input("How old are you?", min_value=1, max_value=120, value=25)
    st.markdown("---")
    leadership_style = st.text_input("How would you describe your leadership style? (e.g., commanding, diplomatic, strategic)")
    core_value = st.text_input("What's most important to you: power, family, honor, or knowledge?")
    conflict_approach = st.text_input("How do you handle conflicts or challenges? (e.g., head-on, strategically, diplomatically)")
    loyalty_approach = st.text_input("What's your approach to loyalty and trust?")
    decision_style = st.text_input("How do you make important decisions? (e.g., logic, emotions, intuition)")
    core_motivation = st.text_input("In a world where power is everything, are you driven primarily by the pursuit of influence and control, or by the desire for security and a peaceful life?")
    submitted = st.form_submit_button("Reveal My Destiny!")

if submitted:
    with st.spinner("Consulting the ancient tomes of Westeros..."):
        context = {
            "user_info": {
                "name": user_name,
                "age": user_age
            },
            "questionnaire_responses": {
                "leadership_style": leadership_style,
                "core_value": core_value,
                "conflict_approach": conflict_approach,
                "loyalty_approach": loyalty_approach,
                "decision_style": decision_style,
                "core_motivation": core_motivation
            },
            "timestamp": str(datetime.now().isoformat())
        }
        crew = GotCharacterMatcher()
        crew_instance = crew.crew()
        try:
            result = crew_instance.kickoff(inputs=context)
            # Extract content
            if hasattr(result, 'raw_output') and result.raw_output:
                content = result.raw_output
            elif hasattr(result, 'output') and result.output:
                content = result.output
            else:
                content = str(result)
            # Clean up
            content = content.replace('```', '').strip('"\'\n ')
            st.markdown("""---""")
            st.markdown(content)
            st.success("May your dragon soar high above the clouds of Westeros! 🏰🐉")
        except Exception as e:
            st.error(f"An error occurred: {e}")
