"""
FastAPI Server

Exposes LangGraph agent system as REST API.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from core.graph import build_graph

app = FastAPI(title="Agentic AI System")

# Build LangGraph app once at startup
agent_app = build_graph()


class CompanyRequest(BaseModel):
    company: str


@app.post("/analyze")
def analyze_company(request: CompanyRequest):
    """
    Analyze a company using multi-agent workflow.
    """

    result = agent_app.invoke({
        "company": request.company
    })

    return {
        "company": request.company,
        "analysis": result.get("analysis", "")
    }
