from core.agent import BaseAgent
from google.genai import types

class ScoutAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Scout", 
            role="Intelligence Researcher", 
            model_name="gemini-2.5-flash" 
        )

    async def research(self, prospect_name: str, company: str) -> str:
        prompt = (
            f"Research {prospect_name} at {company}. "
            f"Identify 3 unique, non-obvious business triggers for a high-end B2B sales outreach. "
            f"Consider: recent strategic initiatives, competitive pressures, growth signals, "
            f"technology adoption patterns, and any publicly known pain points or opportunities. "
            f"Be specific — avoid generic statements. Use concrete details."
        )
        # Enable real-time Google Search Grounding
        tools = [types.Tool(google_search=types.GoogleSearch())]
        
        research_report = await self.chat(prompt, tools=tools)
        return research_report
