"use client";

import { useState, useEffect, useRef } from "react";

interface Log {
  agent: string;
  message: string;
}

export default function Home() {
  const [prospect, setProspect] = useState("");
  const [company, setCompany] = useState("");
  const [logs, setLogs] = useState<Log[]>([]);
  const [isRunning, setIsRunning] = useState(false);
  const [result, setResult] = useState<any>(null);
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [logs]);

  const runMission = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsRunning(true);
    setLogs([{ agent: "System", message: `Initializing mission for ${prospect}...` }]);
    setResult(null);

    try {
      const apiUrl = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";
      const response = await fetch(`${apiUrl}/run-mission`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prospect_name: prospect, company: company }),
      });

      if (!response.ok) throw new Error("Backend connection failed");
      
      const reader = response.body?.getReader();
      const decoder = new TextDecoder();

      if (reader) {
        while (true) {
          const { done, value } = await reader.read();
          if (done) break;
          
          const chunk = decoder.decode(value);
          const lines = chunk.split("\n\n");
          
          for (const line of lines) {
            if (line.startsWith("data: ")) {
              const data = JSON.parse(line.replace("data: ", ""));
              if (data.type === "log") {
                setLogs(prev => [...prev, { agent: data.agent, message: data.message }]);
              } else if (data.type === "result") {
                setResult(data);
              }
            }
          }
        }
      }
    } catch (err) {
      setLogs(prev => [...prev, { agent: "Error", message: "Could not connect to Agentic-Reach backend. Ensure it is running at localhost:8000." }]);
    } finally {
      setIsRunning(false);
    }
  };

  return (
    <main className="min-h-screen p-8 max-w-6xl mx-auto flex flex-col gap-8">
      {/* Header */}
      <header className="flex justify-between items-center">
        <div>
          <h1 className="text-4xl font-bold tracking-tight text-white">
            Agentic-Reach <span className="text-emerald-400">v2026</span>
          </h1>
          <p className="text-slate-400 mt-2">Autonomous Multi-Agent Sales Pod</p>
        </div>
        <div className="px-4 py-2 glass border-emerald-500/50 text-emerald-400 text-sm font-mono flex items-center gap-2">
          <div className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
          SYSTEM_READY
        </div>
      </header>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 flex-grow">
        {/* Left Column: Mission Control */}
        <div className="lg:col-span-4 flex flex-col gap-6">
          <div className="glass p-6 flex flex-col gap-6 glow-card">
            <h2 className="text-xl font-semibold flex items-center gap-2">
              <span className="text-emerald-400">01</span> Mission Target
            </h2>
            <form onSubmit={runMission} className="flex flex-col gap-4">
              <div>
                <label className="text-xs font-bold text-slate-500 uppercase tracking-wider mb-1 block">Prospect Name</label>
                <input 
                  type="text" 
                  value={prospect}
                  onChange={(e) => setProspect(e.target.value)}
                  placeholder="e.g. Sundar Pichai" 
                  className="w-full bg-slate-900 border border-slate-700 rounded-lg p-3 text-white focus:outline-none focus:border-emerald-500 transition-colors"
                />
              </div>
              <div>
                <label className="text-xs font-bold text-slate-500 uppercase tracking-wider mb-1 block">Company</label>
                <input 
                  type="text" 
                  value={company}
                  onChange={(e) => setCompany(e.target.value)}
                  placeholder="e.g. Google" 
                  className="w-full bg-slate-900 border border-slate-700 rounded-lg p-3 text-white focus:outline-none focus:border-emerald-500 transition-colors"
                />
              </div>
              <button 
                type="submit"
                disabled={isRunning || !prospect || !company}
                className={`mt-4 w-full py-4 rounded-lg font-bold text-white transition-all transform active:scale-95 ${
                  isRunning 
                    ? "bg-slate-700 cursor-not-allowed" 
                    : "bg-emerald-600 hover:bg-emerald-500 hover:shadow-[0_0_20px_rgba(16,185,129,0.4)]"
                }`}
              >
                {isRunning ? "MISSION IN PROGRESS..." : "LAUNCH MISSION"}
              </button>
            </form>
          </div>

          {/* Stats/Metrics (Mock) */}
          <div className="glass p-6">
            <h3 className="text-slate-500 text-sm font-bold uppercase mb-4">Pod Metrics</h3>
            <div className="grid grid-cols-2 gap-4">
              <div className="bg-slate-900/50 p-3 rounded-lg border border-slate-800">
                <p className="text-2xl font-bold text-white">4</p>
                <p className="text-xs text-slate-500">Active Agents</p>
              </div>
              <div className="bg-slate-900/50 p-3 rounded-lg border border-slate-800">
                <p className="text-2xl font-bold text-white">3.1</p>
                <p className="text-xs text-slate-500">Model Series</p>
              </div>
            </div>
          </div>
        </div>

        {/* Right Column: The War Room */}
        <div className="lg:col-span-8 flex flex-col gap-6">
          <div className="glass flex-grow flex flex-col overflow-hidden min-h-[500px]">
            <div className="border-b border-white/5 p-4 flex justify-between items-center bg-white/5">
              <h2 className="font-mono text-sm tracking-widest text-emerald-400">LIVE_MISSION_LOGS</h2>
              <div className="text-[10px] text-slate-500 font-mono">CONNECTION: ENCRYPTED</div>
            </div>
            
            <div 
              ref={scrollRef}
              className="p-6 flex flex-col gap-4 overflow-y-auto font-mono text-sm"
            >
              {logs.length === 0 && (
                <div className="text-slate-600 italic">Waiting for mission launch...</div>
              )}
              {logs.map((log, i) => (
                <div key={i} className="flex gap-4 group">
                  <span className={`font-bold min-w-[100px] ${
                    log.agent === 'Scout' ? 'text-blue-400' :
                    log.agent === 'Mirror' ? 'text-rose-400' :
                    log.agent === 'Scribe' ? 'text-amber-400' :
                    log.agent === 'Psychologist' ? 'text-purple-400' :
                    'text-slate-500'
                  }`}>[{log.agent}]</span>
                  <span className="text-slate-300 group-hover:text-white transition-colors">{log.message}</span>
                </div>
              ))}
              {isRunning && (
                <div className="flex gap-4 animate-pulse">
                  <span className="text-emerald-400 font-bold min-w-[100px]">[Thinking]</span>
                  <span className="text-emerald-400">Agentic swarm processing...</span>
                </div>
              )}
            </div>
          </div>

          {/* Final Output Section */}
          {result && (
            <div className="glass p-6 border-emerald-500/30 bg-emerald-500/5 animate-in fade-in slide-in-from-bottom-4 duration-500">
              <div className="flex justify-between items-center mb-4">
                <h2 className="text-xl font-bold text-white">Final Optimized Outreach</h2>
                <button 
                  onClick={() => navigator.clipboard.writeText(result.final_version)}
                  className="text-xs bg-emerald-600/20 hover:bg-emerald-600/40 text-emerald-400 px-3 py-1 rounded border border-emerald-500/30 transition-colors"
                >
                  COPY_TO_CLIPBOARD
                </button>
              </div>
              <div className="bg-black/40 p-6 rounded-lg font-serif italic text-lg leading-relaxed text-slate-200 border border-white/5">
                {result.final_version}
              </div>
              <div className="mt-4 grid grid-cols-2 gap-4">
                <div className="text-xs text-slate-500">
                  <span className="font-bold text-slate-400">Personality Strategy:</span> {result.strategy?.substring(0, 50)}...
                </div>
                <div className="text-xs text-slate-500 text-right">
                  <span className="font-bold text-slate-400">Iterations:</span> 2 Agents Involved
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </main>
  );
}
