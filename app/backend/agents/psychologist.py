from core.agent import BaseAgent

class PsychologistAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Psychologist",
            role="Persuasion & Stylometric Analyst",
            model_name="gemini-1.5-flash"
        )

    async def analyze_personality(self, research_report: str) -> str:
        prompt = f"""
        Analyze the research report below and build a DISC personality profile for the prospect.
        Define the 'Psychological Hook' we should use in our outreach.
        
        REPORT:
        {research_report}
        """
        return await self.chat(prompt)
