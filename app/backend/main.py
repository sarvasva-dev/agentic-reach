from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.scout import ScoutAgent
from agents.mirror import MirrorAgent
from agents.psychologist import PsychologistAgent
from agents.scribe import ScribeAgent
import asyncio

from core.orchestrator import SalesPodOrchestrator

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Agentic-Reach API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize orchestrator
pod = SalesPodOrchestrator()

class MissionRequest(BaseModel):
    prospect_name: str
    company: str

@app.get("/")
def read_root():
    return {"message": "Agentic-Reach Multi-Agent Engine Online"}

from fastapi.responses import StreamingResponse
import json

@app.post("/run-mission")
async def run_mission(req: MissionRequest):
    async def event_generator():
        async for event in pod.run_mission(req.prospect_name, req.company):
            yield f"data: {json.dumps(event)}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")
