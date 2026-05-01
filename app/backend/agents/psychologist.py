from core.agent import BaseAgent

class PsychologistAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Psychologist", 
            role="Behavioral Analysis Expert", 
            model_name="gemini-2.0-flash"
        )

    async def analyze_personality(self, digital_shadow: str) -> str:
        prompt = (
            f"DIGITAL SHADOW DATA:\n{digital_shadow}\n\n"
            "TASK: Analyze the personality of this individual based on their writing style and social presence. "
            "Determine their DISC profile (Dominance, Influence, Steadiness, Conscientiousness). "
            "Suggest the best 'Persuasion Strategy': Should the pitch be direct and data-heavy, "
            "or visionary and relationship-focused? Provide actionable 'Do's and 'Don'ts' for the outreach."
        )
        response = await self.chat(prompt)
        return response
