from core.agent import BaseAgent

class MirrorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Mirror",
            role="Adversarial Critique Specialist",
            model_name="gemini-1.5-flash"
        )

    async def critique(self, initial_draft: str, strategy: str) -> str:
        prompt = f"""
        Act as a cynical, busy prospect who hates being sold to.
        Critique the initial draft below based on the persuasion strategy.
        
        INITIAL DRAFT:
        {initial_draft}
        
        STRATEGY:
        {strategy}
        
        Point out exactly why you would DELETE this email and how to make it 'uncopyable'.
        """
        return await self.chat(prompt)
