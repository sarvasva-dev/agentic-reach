from core.agent import BaseAgent

class ScribeAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Scribe", 
            role="Expert Copywriter", 
            model_name="gemini-2.5-flash"
        )

    async def draft(self, research: str, strategy: str, feedback: str = None) -> str:
        prompt = f"""
        Write a hyper-personalized sales outreach email.
        
        RESEARCH: {research}
        STRATEGY: {strategy}
        {f'FEEDBACK TO INCORPORATE: {feedback}' if feedback else ''}
        
        Rules:
        - No generic 'I hope this finds you well'.
        - Use the business triggers from research.
        - Match the DISC profile from strategy.
        - Keep it under 100 words.
        """
        return await self.chat(prompt)

    async def rewrite(self, previous_draft: str, critique: str) -> str:
        prompt = (
            f"PREVIOUS DRAFT: {previous_draft}\n"
            f"CRITIQUE FROM PROSPECT: {critique}\n\n"
            "TASK: The prospect rejected your first draft for the reasons above. "
            "Rewrite the message to address all concerns. Make it even more human and authentic. "
            "Avoid all AI cliches (e.g., 'I hope this finds you well', 'In today's fast-paced world')."
        )
        response = await self.chat(prompt)
        return response
