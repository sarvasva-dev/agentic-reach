# 🚀 Agentic-Reach — Autonomous Multi-Agent Sales Intelligence Platform

> **Submission for Google PromptWars x Ascent Hackathon**
> Built by Sarthak Srivastava | [LinkedIn](#)

---

## 🎯 The Problem
Most AI sales tools make outreach *louder*, not *smarter*. They generate high-volume, templated messages that feel robotic. The result? Lower reply rates and damaged sender reputation.

## 💡 The Solution
**Agentic-Reach** deploys a swarm of 4 specialized AI agents that collaborate in a "War Room" to produce *one* hyper-personalized, human-sounding outreach message — one that a real decision-maker would actually reply to.

---

## 🏗️ Architecture: The Sales Pod

```
Prospect Input
     │
     ▼
┌─────────────┐    Google Search    ┌──────────────────┐
│  🕵️ Scout   │ ─── Grounding ────► │  Research Report │
└─────────────┘                     └────────┬─────────┘
                                             │
                                    ┌────────▼─────────┐
                                    │ 🧠 Psychologist  │
                                    │  DISC Profiling  │
                                    └────────┬─────────┘
                                             │
                                    ┌────────▼─────────┐
                                    │  ✍️ Scribe        │
                                    │  Initial Draft   │
                                    └────────┬─────────┘
                                             │
                                    ┌────────▼─────────┐
                                    │  🎭 Mirror       │
                                    │  Adversarial     │◄─── Cynical Prospect
                                    │  Critique Loop   │     Simulation
                                    └────────┬─────────┘
                                             │ (Rewrite)
                                    ┌────────▼─────────┐
                                    │  ✍️ Scribe        │
                                    │  FINAL VERSION   │
                                    └──────────────────┘
```

### Agents
| Agent | Model | Role |
|---|---|---|
| 🕵️ **Scout** | Gemini 2.5 Flash | Deep research with Google Search Grounding |
| 🧠 **Psychologist** | Gemini 2.0 Flash | DISC personality analysis & persuasion strategy |
| 🎭 **Mirror** | Gemini 2.0 Flash | Simulates the cynical prospect — adversarial critic |
| ✍️ **Scribe** | Gemini 2.5 Flash | Expert copywriting & iterative rewriting |

---

## 🛠️ Google Tech Stack
- **Gemini 2.5 Flash** — High-reasoning synthesis for research and final copy
- **Gemini 2.0 Flash** — High-velocity iterations for critique and personality loops
- **Google Search Grounding** — Real-time, grounded business intelligence (architectural integration)
- **FastAPI** — High-performance Python async backend
- **Next.js 15** — React frontend with real-time SSE streaming

---

## 📊 Key Innovation: Real-Time War Room

The frontend streams agent logs **live** using Server-Sent Events (SSE) as the agents debate and refine the outreach:

```
[System]      Initializing mission for Sundar Pichai at Google...
[Scout]       Deep searching for business triggers via Google Search Grounding...
[Scout]       Research complete. 3 business triggers identified.
[Psychologist] Analyzing behavioral patterns and DISC profile...
[Psychologist] Profile: High-D executive. ROI-first, peer tone.
[Scribe]      Drafting initial outreach message...
[Mirror]      REJECTED: Too generic. No concrete proof points.
[Scribe]      Self-correcting... Final version optimized. ✓
```

---

## 🚀 Running Locally

### Backend
```bash
cd app/backend
pip install -r requirements.txt
cp .env.example .env        # Add your GOOGLE_API_KEY
uvicorn main:app --reload
```

### Frontend
```bash
cd app/frontend
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000)

---

## ☁️ Deployment

| Service | Platform | Status |
|---|---|---|
| Backend API | Render.com | `render.yaml` included |
| Frontend | Vercel | Auto-deploy from GitHub |

### Deploy Backend to Render
1. Push repo to GitHub
2. Go to [render.com](https://render.com) → New Web Service → Connect repo
3. Set root directory: `app/backend`
4. Add env var: `GOOGLE_API_KEY=your_key`
5. Deploy ✓

### Deploy Frontend to Vercel
1. Go to [vercel.com](https://vercel.com) → Import repo
2. Set root directory: `app/frontend`
3. Add env var: `NEXT_PUBLIC_API_URL=https://your-render-url.onrender.com`
4. Deploy ✓

---

## 🧪 Testing

```bash
cd app/backend
python -m pytest tests/ -v
```

**5 tests, all passing:**
- ✅ Module imports
- ✅ Demo mode orchestration
- ✅ SSE event stream structure
- ✅ Result field validation
- ✅ Request model validation

---

## 📁 Project Structure

```
app/
├── backend/
│   ├── agents/
│   │   ├── scout.py          # Google Search Grounding research
│   │   ├── psychologist.py   # DISC personality analysis
│   │   ├── mirror.py         # Adversarial critique simulation
│   │   └── scribe.py         # Expert copywriting
│   ├── core/
│   │   ├── agent.py          # BaseAgent class
│   │   └── orchestrator.py   # Multi-agent pipeline controller
│   ├── tests/
│   │   └── test_orchestrator.py
│   ├── main.py               # FastAPI with SSE streaming
│   ├── requirements.txt
│   └── render.yaml           # Render deployment config
└── frontend/
    └── src/app/
        ├── page.tsx           # War Room dashboard
        └── globals.css        # Dark glassmorphism theme
```

---

## 🔐 Security
- API keys loaded from environment variables only
- `.env` excluded from version control via `.gitignore`
- CORS configured for production domains

---

*Built with 💜 using Google AI Studio, Gemini 2.x series, FastAPI, and Next.js*