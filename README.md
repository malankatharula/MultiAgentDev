---
title: MultiAgent DevOps Assistant
emoji: 🤖
colorFrom: purple
colorTo: blue
sdk: docker
pinned: false
---



# 🤖 MultiAgent DevOps Assistant

An AI-powered multi-agent system that routes developer tasks to specialized agents using **LangGraph** orchestration and **Groq** (Llama 3.3 70B).

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green?style=flat-square&logo=fastapi)
![LangGraph](https://img.shields.io/badge/LangGraph-0.1-purple?style=flat-square)
![Groq](https://img.shields.io/badge/Groq-Llama_3.3_70B-orange?style=flat-square)


live on : https://huggingface.co/spaces/malankabuilder/MultiAgentDev
---

##  Architecture

```     
User Task (natural language)
         ↓
 Orchestrator Agent  ←── LangGraph StateGraph
         ↓
 routes based on task type
         ↓
┌────────────────────────────────────┐
│  Code Agent   → writes clean code  │
│  Debug Agent  → finds root cause   │
│  Doc Agent    → generates docs     │
│  Test Agent   → writes pytest      │
└────────────────────────────────────┘
         ↓
  Result rendered in UI
```

##  Features

- **Intelligent routing** - orchestrator classifies task and routes to the right agent automatically
- **4 specialized agents** - each with a focused system prompt for their domain
- **LangGraph state machine** - shared state flows through the graph, every agent reads and writes
- **Groq inference** - Llama 3.3 70B for fast, high-quality responses
- **Syntax-highlighted UI** - dark terminal aesthetic, markdown rendering, live agent log

##  Stack

| Layer | Technology |
|---|---|
| Agent Orchestration | LangGraph |
| LLM | Groq API (Llama 3.3 70B) |
| Backend | FastAPI |
| Frontend | HTML / CSS / JS |
| LLM Framework | LangChain |

## 🚀 Run Locally

```bash
# 1. Clone
git clone https://github.com/malankatharula/MultiAgentDev
cd MultiAgentDev

# 2. Install
pip install langgraph langchain-groq langchain-core fastapi uvicorn python-dotenv

# 3. Set env
echo GROQ_API_KEY=your_key_here > .env

# 4. Run
uvicorn main:app --reload --port 8080
```

Open `http://localhost:8080`

## 📁 Project Structure

```
MultiAgentDev/
├── main.py                  # FastAPI app entry point
├── graph/
│   ├── state.py             # Shared AgentState (TypedDict)
│   ├── orchestrator.py      # Routes task to correct agent
│   ├── graph_builder.py     # LangGraph StateGraph definition
│   └── agents/
│       ├── code_agent.py
│       ├── debug_agent.py
│       ├── doc_agent.py
│       └── test_agent.py
├── api/
│   └── routes.py            # POST /api/run endpoint
└── frontend/
    └── index.html           # Single-page UI
```

## 👤 Author

**Malanka Tharula Wickramasinghe**  
[GitHub](https://github.com/malankatharula) · [LinkedIn](https://linkedin.com/in/malanka-tharula-b329432a7)