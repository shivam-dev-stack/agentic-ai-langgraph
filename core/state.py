"""
Shared Agent State Definition

Defines the structure of data passed between LangGraph nodes.
"""

from typing import TypedDict


class AgentState(TypedDict):
    """
    AgentState maintains context between agents.

    Fields:
        company: User-provided company name
        raw_data: Collected company information
        analysis: Final analytical output
    """

    company: str
    raw_data: str
    analysis: str
