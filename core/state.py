"""
Shared Agent State Definition

Defines the structure of data passed between LangGraph nodes.
"""

from typing import TypedDict


class AgentState(TypedDict):
    """
    AgentState maintains agents.

    Fields:
        company: company name
        raw_data: Collected company information
        analysis: Final output
    """

    company: str
    raw_data: str
    analysis: str
