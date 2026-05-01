# SPEC.md — Agentic-Reach

> **Status**: `FINALIZED`
> **Project**: Google PromptWars x Ascent (Sales Vertical)
> **Model Generation**: Gemini 3.1 Series (May 2026 Edition)

## Vision
To build the world's first "Autonomous Sales Pod" that eliminates AI-generated spam by using a self-correcting multi-agent swarm. Agentic-Reach uses deep research, psychological profiling, and adversarial role-playing to create outreach that is indistinguishable from a top-tier human consultant.

## Goals
1. **Autonomous Research:** Leverage Gemini 3.1 Pro + Native Google Search Grounding to find non-obvious business triggers (news, filings, social signals).
2. **Psychological Mirroring:** Analyze prospect writing styles to map personality types (DISC/OCEAN) and adapt the pitch tone.
3. **Adversarial Critique:** Implement "Agent Mirror"—a cynical digital twin of the prospect that tries to find reasons to ignore the email, forcing the system to self-correct.
4. **Premium "War Room" UI:** A real-time dashboard showing agents collaborating, debating, and finalizing the "Perfect Pitch."

## Non-Goals (Out of Scope)
- Bulk email sending (focus is on quality, not volume).
- CRM integration (v1 will provide export/copy-paste).
- Linked-In automation (v1 will avoid risky browser automation).

## Users
- **B2B Sales Development Reps (SDRs):** Who need high-quality hooks for high-value accounts.
- **Founders:** Doing manual outreach who want a "ghostwriter" that actually thinks like them.

## Constraints
- **Model**: Must use Gemini 3 / 3.1 series (Gemini 3.1 Pro for synthesis, Gemini 3 Flash for iterations).
- **Budget**: Keep token usage optimized using Gemini 3 Flash for iterative agent loops.
- **Timeline:** Submission due in 7 days (May 8, 2026).

## Success Criteria
- [ ] Successful multi-agent workflow (Scout -> Psychologist -> Mirror -> Scribe).
- [ ] Native integration of Google Search Grounding.
- [ ] "Pass/Fail" logic for the Mirror Agent with at least 3 iterations of self-correction.
- [ ] 100% "Human-like" score on AI detection (informal benchmark).
- [ ] Deployed link on Cloud Run (or Vercel fallback).
