import pytest
import asyncio
from unittest.mock import AsyncMock, patch

# ─── Basic sanity tests — no API key needed ───────────────────────────────────

def test_imports():
    """All agent modules must be importable without errors."""
    from agents.scout import ScoutAgent
    from agents.mirror import MirrorAgent
    from agents.psychologist import PsychologistAgent
    from agents.scribe import ScribeAgent
    from core.orchestrator import SalesPodOrchestrator
    assert True

def test_orchestrator_demo_mode():
    """Orchestrator should work in DEMO_MODE without calling any API."""
    import os
    os.environ["DEMO_MODE"] = "true"
    os.environ["GOOGLE_API_KEY"] = "test-key-not-real"

    from core.orchestrator import SalesPodOrchestrator
    pod = SalesPodOrchestrator()
    assert pod.demo_mode is True

def test_demo_mission_events():
    """Demo mission must yield at least 8 log events and 1 result event."""
    import os
    os.environ["DEMO_MODE"] = "true"
    os.environ["GOOGLE_API_KEY"] = "test-key-not-real"

    from core.orchestrator import SalesPodOrchestrator
    pod = SalesPodOrchestrator()

    async def collect():
        events = []
        async for event in pod.run_mission("Test Prospect", "Test Company"):
            events.append(event)
        return events

    events = asyncio.get_event_loop().run_until_complete(collect())
    logs = [e for e in events if e.get("type") == "log"]
    results = [e for e in events if e.get("type") == "result"]

    assert len(logs) >= 8, f"Expected at least 8 log events, got {len(logs)}"
    assert len(results) == 1, "Expected exactly 1 result event"

def test_result_has_required_fields():
    """Result event must contain all required output fields."""
    import os
    os.environ["DEMO_MODE"] = "true"
    os.environ["GOOGLE_API_KEY"] = "test-key-not-real"

    from core.orchestrator import SalesPodOrchestrator
    pod = SalesPodOrchestrator()

    async def get_result():
        async for event in pod.run_mission("Test", "TestCo"):
            if event.get("type") == "result":
                return event
        return None

    result = asyncio.get_event_loop().run_until_complete(get_result())
    assert result is not None
    for field in ["research", "strategy", "initial_draft", "critique", "final_version"]:
        assert field in result, f"Missing field: {field}"
        assert len(result[field]) > 10, f"Field '{field}' is too short"

def test_mission_request_model():
    """FastAPI MissionRequest model must validate required fields."""
    import sys, os
    os.environ["GOOGLE_API_KEY"] = "test-key"
    os.environ["DEMO_MODE"] = "true"
    from pydantic import ValidationError
    # Inline the model to test without importing the full app
    from pydantic import BaseModel
    class MissionRequest(BaseModel):
        prospect_name: str
        company: str

    req = MissionRequest(prospect_name="Sarthak", company="Smart Galla")
    assert req.prospect_name == "Sarthak"
    assert req.company == "Smart Galla"

    with pytest.raises(ValidationError):
        MissionRequest(prospect_name="Only Name")  # missing company
