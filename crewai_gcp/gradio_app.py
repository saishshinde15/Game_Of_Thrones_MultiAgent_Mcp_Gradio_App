import gradio as gr
from crewai_gcp.crew import GotCharacterMatcher
from datetime import datetime

def got_matcher_interface(user_name, user_age, leadership_style, core_value, conflict_approach, loyalty_approach, decision_style, core_motivation):
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
        if hasattr(result, 'raw_output') and result.raw_output:
            content = result.raw_output
        elif hasattr(result, 'output') and result.output:
            content = result.output
        else:
            content = str(result)
        content = content.replace('```', '').strip('"\'\n ')
        return content
    except Exception as e:
        return f"An error occurred: {e}"


got_style_note = (
    """
    ⚔️ **A Raven Arrives with a Warning:**
    
    The ancient tomes of Westeros are vast, and the Maesters are thorough. Your destiny will be revealed, but such magic takes a minute or two. 
    
    _"Patience, for even dragons must wait for the fire to rise..."_
    """
)

iface = gr.Interface(
    fn=got_matcher_interface,
    inputs=[
        gr.Textbox(label="What's your name?"),
        gr.Number(label="How old are you?", value=25),
        gr.Textbox(label="How would you describe your leadership style? (e.g., commanding, diplomatic, strategic)"),
        gr.Textbox(label="What's most important to you: power, family, honor, or knowledge?"),
        gr.Textbox(label="How do you handle conflicts or challenges? (e.g., head-on, strategically, diplomatically)"),
        gr.Textbox(label="What's your approach to loyalty and trust?"),
        gr.Textbox(label="How do you make important decisions? (e.g., logic, emotions, intuition)"),
        gr.Textbox(label="In a world where power is everything, are you driven primarily by the pursuit of influence and control, or by the desire for security and a peaceful life?")
    ],
    outputs=gr.Markdown(label="Your Game of Thrones Destiny"),
    title="Game of Thrones Character & Dragon Matcher 🏰🐉",
    description="Answer a few questions and discover which Game of Thrones character and dragon you truly are!",
    article=got_style_note
)

if __name__ == "__main__":
    iface.launch()
