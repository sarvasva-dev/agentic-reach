from core.agent import BaseAgent

class ScribeAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Scribe", 
            role="Expert Sales Copywriter", 
            model_name="gemini-2.5-flash"
        )

    async def draft_outreach(self, context: str, strategy: str) -> str:
        prompt = (
            f"BUSINESS CONTEXT: {context}\n"
            f"PERSUASION STRATEGY: {strategy}\n\n"
            "TASK: Draft a hyper-personalized LinkedIn outreach message. "
            "It must feel human, non-spammy, and demonstrate deep research. "
            "Use a specific 'Hook' from the context. Keep it under 150 words."
        )
        response = await self.chat(prompt)
        return response

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
