import os
import asyncio
from typing import List, Dict, Any, Optional
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class BaseAgent:
    def __init__(self, name: str, role: str, model_name: str = "gemini-2.0-flash"):
        """
        Base class for Agentic-Reach agents.
        Using gemini-2.x-flash for high quota and reliability in 2026.
        """
        self.name = name
        self.role = role
        self.model_name = "gemini-2.0-flash" if model_name in ["gemini-1.5-flash", "gemini-3-flash-preview"] else model_name
        
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError(f"Agent {name} needs GOOGLE_API_KEY")
            
        genai.configure(api_key=api_key)
        
        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            system_instruction=f"You are {self.name}, acting as the {self.role}. Your mission is to assist in creating hyper-personalized sales outreach."
        )

    async def chat(self, prompt: str, context: Optional[str] = None) -> str:
        """Async chat interface — runs sync Gemini call in a thread pool."""
        full_prompt = prompt
        if context:
            full_prompt = f"Context: {context}\n\nTask: {prompt}"
            
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(None, self.model.generate_content, full_prompt)
        return response.text

    def __repr__(self):
        return f"<Agent {self.name} ({self.role})>"
