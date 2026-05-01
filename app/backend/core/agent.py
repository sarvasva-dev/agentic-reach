import os
import asyncio
from typing import List, Dict, Any, Optional
from google import genai
from google.genai import types
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor

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
            
        self.client = genai.Client(api_key=api_key)
        self.system_instruction = f"You are {self.name}, acting as the {self.role}. Your mission is to assist in creating hyper-personalized sales outreach."
        self.executor = ThreadPoolExecutor(max_workers=5)

    async def chat(self, prompt: str, context: Optional[str] = None) -> str:
        """Async chat interface — runs modern SDK Gemini call in a thread pool."""
        full_prompt = prompt
        if context:
            full_prompt = f"Context: {context}\n\nTask: {prompt}"
            
        loop = asyncio.get_event_loop()
        
        def call_gemini():
            return self.client.models.generate_content(
                model=self.model_name,
                contents=full_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=self.system_instruction
                )
            )

        response = await loop.run_in_executor(self.executor, call_gemini)
        return response.text

    def __repr__(self):
        return f"<Agent {self.name} ({self.role})>"
