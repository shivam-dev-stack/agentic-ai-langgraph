# Agentic AI System – Multi-Agent Workflow using LangGraph


## Features

- Multi-agent architecture (Collector + Analyst)
- LangGraph orchestration
- Shared typed state between agents
- FastAPI backend with Swagger UI
- Deterministic execution using mocked data (no external API keys required)
- Modular folder structure
- Demo notebook for reproducibility

---

## Architecture

### System Overview

The system consists of:

- **Collector Agent** – gathers company-related data (mocked)
- **Analyst Agent** – analyzes data and generates insights
- **LangGraph Orchestrator** – manages execution flow
- **FastAPI Service** – exposes REST endpoint

---

### Agent Workflow
```bash
User / API Request
|
v
+------------------+
| Collector Agent |
+------------------+
|
v
+----------------+
| Analyst Agent |
+----------------+
|
v
Final Report
```

---

### Component Responsibilities

#### Collector Agent
Fetches company news and market data (implemented using local dummy data to avoid API dependencies).

#### Analyst Agent
Generates:
- Summary
- Risks
- Opportunities
- Overall insight

#### LangGraph Orchestrator
Controls agent execution order and maintains shared state.

#### FastAPI Layer
Provides `/analyze` endpoint to trigger the workflow.

---

###  State Management

LangGraph uses a typed shared state:

AgentState:

company

raw_data

analysis


---

### Design Principles

- Explicit agent roles
- Deterministic workflow
- Separation of concerns
- Reproducible execution
- Production-style API interface

---

##  Project Structure
```bash
agentic-ai-system/
│
├── agents/
│ ├── collector.py
│ └── analyst.py
│
├── core/
│ ├── state.py
│ └── graph.py
│
├── api/
│ └── main.py
│
├── data/
│ └── dummy_data.py
│
├── notebooks/
│ └── demo.ipynb
│
├── requirements.txt
├── run.py
└── README.md
```

---

## Setup Instructions
```bash
1. Create virtual environment


python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

2. Install dependencies
pip install -r requirements.txt

3. Run API Server
uvicorn api.main:app --reload


Open browser:

http://127.0.0.1:8000/docs


Use /analyze endpoint.

Example Request
{
  "company": "Tesla"
}

 CLI Execution

python run.py

Notebook Demo

Open:

notebooks/demo.ipynb


Run cells to see agent workflow in action.

---



