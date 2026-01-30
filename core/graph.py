"""
LangGraph Orchestrator

Defines the multi-agent workflow:
Collector Agent -> Analyst Agent
"""

from langgraph.graph import StateGraph
from core.state import AgentState
from agents.collector import collector
from agents.analyst import analyst


def build_graph():
    """
    Builds and compiles the LangGraph workflow.
    """

    graph = StateGraph(AgentState)

    # Register agents as nodes
    graph.add_node("collector", collector)
    graph.add_node("analyst", analyst)

    # Define flow
    graph.set_entry_point("collector")
    graph.add_edge("collector", "analyst")

    # Compile graph
    app = graph.compile()

    return app
