"""
Collector Agent

Responsibility:
Fetch company-related data (news + stock performance).

In this implementation, external APIs are mocked using local dummy data
to ensure reproducibility without API keys.
"""

from data.dummy_data import get_company_data


def collector(state):
    """
    LangGraph node function.

    Input:
        state: AgentState (expects 'company')

    Output:
        Updates state with 'raw_data'
    """

    company = state["company"].title()

    company_data = get_company_data(company)

    return {
        "raw_data": company_data
    }
