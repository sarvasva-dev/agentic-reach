from core.agent import BaseAgent
import google.generativeai as genai
import asyncio

class ScoutAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Scout", 
            role="Deep Intelligence Researcher", 
            model_name="gemini-2.5-flash" 
        )
        
        # Rebuild model with specialized research system instruction
        # Note: Search Grounding is the architectural goal; the model's
        # vast training knowledge is used for the local demo.
        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            system_instruction=(
                "You are Scout, the lead intelligence agent for Agentic-Reach. "
                "You have deep knowledge of business landscapes, corporate strategy, funding rounds, "
                "product launches, and executive profiles. "
                "Your job is to find 3 non-obvious, highly specific business triggers for a prospect. "
                "Think like a top-tier enterprise sales researcher. "
                "Always format your output as: TRIGGER 1: [title] - [detail]. TRIGGER 2: ... TRIGGER 3: ..."
            )
        )

    async def research(self, prospect_name: str, company: str) -> str:
        prompt = (
            f"Research {prospect_name} at {company}. "
            f"Identify 3 unique, non-obvious business triggers for a high-end B2B sales outreach. "
            f"Consider: recent strategic initiatives, competitive pressures, growth signals, "
            f"technology adoption patterns, and any publicly known pain points or opportunities. "
            f"Be specific — avoid generic statements. Use concrete details."
        )
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(None, self.model.generate_content, prompt)
        return response.text
