from mcp.server.fastmcp import FastMCP
from crewai_gcp.crew import GotCharacterMatcher
from datetime import datetime

def got_matcher_mcp(user_info: dict, questionnaire_responses: dict) -> str:
    context = {
        "user_info": user_info,
        "questionnaire_responses": questionnaire_responses,
        "timestamp": str(datetime.now().isoformat())
    }
    crew = GotCharacterMatcher()
    crew_instance = crew.crew()
    result = crew_instance.kickoff(inputs=context)
    if hasattr(result, 'raw_output') and result.raw_output:
        content = result.raw_output
    elif hasattr(result, 'output') and result.output:
        content = result.output
    else:
        content = str(result)
    return content.replace('```', '').strip('"\'\n ')

# Create FastMCP instance
mcp = FastMCP("got_matcher")

@mcp.tool()
def match_got_character(user_info: dict, questionnaire_responses: dict) -> str:
    """
    Run the Game of Thrones matcher via CrewAI.

    Args:
        user_info (dict): User info (name, age, etc.)
        questionnaire_responses (dict): Answers to all questions.

    Returns:
        str: The story-driven result.
    """
    return got_matcher_mcp(user_info, questionnaire_responses)

# Run the server
if __name__ == "__main__":
    mcp.run(transport="stdio")
