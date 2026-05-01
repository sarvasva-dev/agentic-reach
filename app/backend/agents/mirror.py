from core.agent import BaseAgent

class MirrorAgent(BaseAgent):
    def __init__(self):
        # Flash is great for the Mirror because we might iterate multiple times
        super().__init__(
            name="Mirror", 
            role="Cynical Prospect Persona", 
            model_name="gemini-2.0-flash"
        )

    async def critique(self, email_draft: str, prospect_context: str) -> dict:
        prompt = (
            f"PROSPECT CONTEXT: {prospect_context}\n\n"
            f"EMAIL DRAFT:\n{email_draft}\n\n"
            "TASK: You are the busy, cynical prospect described in the context. "
            "Critique this email. Why would you ignore it? Does it feel like a template? "
            "Be harsh but fair. Provide a 'Boredom Score' (1-10) and specific reasons for rejection."
            "\nReturn your response in a clear format with 'SCORE' and 'CRITIQUE'."
        )
        response = await self.chat(prompt)
        return {"response": response}
