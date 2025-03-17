from phi.agent import Agent
from phi.model.google import Gemini

image_text_agent = Agent(
    model=Gemini(id="gemini-1.5-flash"),
    markdown=False,
    structured_outputs=True,
    parse_response=True,
)
