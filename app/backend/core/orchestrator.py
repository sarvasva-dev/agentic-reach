from agents.scout import ScoutAgent
from agents.psychologist import PsychologistAgent
from agents.scribe import ScribeAgent
from agents.mirror import MirrorAgent
import asyncio
import os

# ---------------------------------------------------------------------------
# DEMO MODE — pre-crafted realistic outputs for demos / quota-exhausted keys
# ---------------------------------------------------------------------------
DEMO_RESEARCH = """
TRIGGER 1: AI-First Retail Transformation — Smart Galla recently pivoted to an 
AI-powered inventory management system (per their latest LinkedIn job postings for 
ML Engineers). This signals a major digital transformation underway that requires 
external expertise.

TRIGGER 2: Series A Funding Pressure — Smart Galla's last funding round was 18 months 
ago, putting them in the classic "scaling pains" phase. They need to demonstrate 
operational efficiency to unlock Series B, which means ROI on every tool matters.

TRIGGER 3: Expanding to Tier-2 Cities — Public data shows Smart Galla recently opened 
3 new warehouse locations in Jaipur and Lucknow, suggesting aggressive expansion where 
outreach automation would be critical for new market penetration.
"""

DEMO_STRATEGY = """
DISC Profile: HIGH D (Dominance) + C (Conscientiousness)
Persuasion Strategy: Lead with ROI numbers and time-to-value. Skip pleasantries.
Avoid: Vague promises, long intros, "AI-powered" buzzwords without proof.
Hook: Reference the Tier-2 expansion specifically — show you did your homework.
Tone: Peer-to-peer. Direct. Data-first. Respect their time.
"""

DEMO_DRAFT = """
Hi Sarthak,

Noticed Smart Galla just opened in Jaipur and Lucknow — bold move in a competitive 
market. That kind of expansion usually means the outreach team is stretched thin trying 
to onboard new enterprise accounts in markets where you have zero brand recall.

We help B2B teams in your exact phase generate personalized outreach at scale — the kind 
that gets responses, not the templated stuff that gets archived.

Worth a 15-minute call this week?
"""

DEMO_CRITIQUE = """
REJECTION REASON: The opening is decent, but "bold move" sounds like flattery. 
I've heard "worth a 15-minute call" 200 times this month. The Jaipur/Lucknow hook 
is strong but then you pivot to generic "personalized outreach at scale" which 
loses all credibility. Give me ONE specific number. Why should I trust you?
"""

DEMO_FINAL = """
Hi Sarthak,

Smart Galla's Jaipur expansion caught my eye — specifically, you're entering a market 
where your enterprise prospect conversion is likely 40% slower than metro markets 
(standard for new-territory B2B).

We helped a similar-stage D2B startup cut that ramp-down to 3 weeks by rebuilding 
their outreach for local decision-maker profiles. Happy to share the exact framework — 
no call needed, I can send it over in 2 minutes if useful.
"""


class SalesPodOrchestrator:
    def __init__(self):
        self.demo_mode = os.getenv("DEMO_MODE", "false").lower() == "true"
        if not self.demo_mode:
            self.scout = ScoutAgent()
            self.psychologist = PsychologistAgent()
            self.scribe = ScribeAgent()
            self.mirror = MirrorAgent()
        self.logs = []

    def log(self, agent: str, message: str):
        print(f"[{agent}] {message}")
        self.logs.append({"agent": agent, "message": message})

    async def run_mission(self, prospect_name: str, company: str):
        self.logs = []

        if self.demo_mode:
            async for event in self._run_demo(prospect_name, company):
                yield event
        else:
            async for event in self._run_live(prospect_name, company):
                yield event

    async def _run_demo(self, prospect_name: str, company: str):
        """Returns pre-crafted realistic demo outputs with real timing."""
        yield {"type": "log", "agent": "System", "message": f"[DEMO] Initializing mission for {prospect_name} at {company}..."}
        await asyncio.sleep(0.5)

        yield {"type": "log", "agent": "Scout", "message": "Activating Google Search Grounding — scanning news, filings, and signals..."}
        await asyncio.sleep(2)
        yield {"type": "log", "agent": "Scout", "message": "Research complete. 3 unique business triggers identified."}
        await asyncio.sleep(0.3)

        yield {"type": "log", "agent": "Psychologist", "message": "Analyzing behavioral patterns and DISC personality profile..."}
        await asyncio.sleep(1.5)
        yield {"type": "log", "agent": "Psychologist", "message": "Profile: High-D executive. Strategy: ROI-first, peer tone, no fluff."}
        await asyncio.sleep(0.3)

        yield {"type": "log", "agent": "Scribe", "message": "Drafting initial outreach message based on research and strategy..."}
        await asyncio.sleep(2)
        yield {"type": "log", "agent": "Scribe", "message": "Draft ready. Routing to Mirror agent for adversarial critique."}
        await asyncio.sleep(0.3)

        yield {"type": "log", "agent": "Mirror", "message": "Simulating cynical prospect reaction — stress-testing the draft..."}
        await asyncio.sleep(1.5)
        yield {"type": "log", "agent": "Mirror", "message": "REJECTED: 'Worth a 15-min call' is overused. No concrete numbers provided."}
        await asyncio.sleep(0.3)

        yield {"type": "log", "agent": "Scribe", "message": "Applying Mirror corrections — removing clichés, adding proof points..."}
        await asyncio.sleep(2)
        yield {"type": "log", "agent": "Scribe", "message": "Mission accomplished. Final version passed adversarial review."}

        yield {
            "type": "result",
            "research": DEMO_RESEARCH.strip(),
            "strategy": DEMO_STRATEGY.strip(),
            "initial_draft": DEMO_DRAFT.strip(),
            "critique": DEMO_CRITIQUE.strip(),
            "final_version": DEMO_FINAL.strip()
        }

    async def _run_live(self, prospect_name: str, company: str):
        """Full live agentic pipeline."""
        self.log("System", f"Starting mission for {prospect_name} at {company}...")
        yield {"type": "log", "agent": "System", "message": f"Starting mission for {prospect_name} at {company}..."}

        self.log("Scout", "Deep searching for business triggers...")
        yield {"type": "log", "agent": "Scout", "message": "Deep searching for business triggers via Google Search Grounding..."}
        research_report = await self.scout.research(prospect_name, company)
        yield {"type": "log", "agent": "Scout", "message": "Research complete. Analysis synthesized."}

        self.log("Psychologist", "Analyzing personality shadow...")
        yield {"type": "log", "agent": "Psychologist", "message": "Analyzing behavioral patterns and personality DISC profile..."}
        strategy = await self.psychologist.analyze_personality(research_report)
        yield {"type": "log", "agent": "Psychologist", "message": "Strategy defined. Tone adjusted for prospect personality."}

        self.log("Scribe", "Drafting initial outreach...")
        yield {"type": "log", "agent": "Scribe", "message": "Drafting initial outreach message..."}
        draft = await self.scribe.draft_outreach(research_report, strategy)
        yield {"type": "log", "agent": "Scribe", "message": "Initial draft ready. Submitting for adversarial review."}

        self.log("Mirror", "Critiquing draft as the prospect...")
        yield {"type": "log", "agent": "Mirror", "message": "Entering Mirror mode. Simulating cynical prospect reaction..."}
        critique_result = await self.mirror.critique(draft, research_report)
        critique = critique_result["response"]
        yield {"type": "log", "agent": "Mirror", "message": "Critique finished. Sending corrections back to Scribe."}

        self.log("Scribe", "Applying corrections for final version...")
        yield {"type": "log", "agent": "Scribe", "message": "Self-correcting based on Mirror feedback..."}
        final_version = await self.scribe.rewrite(draft, critique)
        yield {"type": "log", "agent": "Scribe", "message": "Mission accomplished. Final version optimized."}

        yield {
            "type": "result",
            "research": research_report,
            "strategy": strategy,
            "initial_draft": draft,
            "critique": critique,
            "final_version": final_version
        }
