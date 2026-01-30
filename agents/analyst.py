from datetime import datetime

"""
Analyst Agent

Responsibility:
Analyze collected company data and generate:
- Summary
- Risks
- Opportunities

LLM responses are mocked for reproducibility.
"""

def analyst(state):
    """
    LangGraph node function.

    Input:
        state: AgentState (expects 'raw_data')

    Output:
        Updates state with 'analysis'
    """

    now = datetime.utcnow().isoformat()


    raw_data = state["raw_data"]

    analysis = f"""
Company Intelligence Report

SUMMARY:
{raw_data}

RISKS:
- Market volatility may impact short-term stock performance.
- High competition in AI-driven product space.
- Dependency on successful product launches.

OPPORTUNITIES:
- Expansion into emerging markets.
- Growth potential from new AI offerings.
- Increasing demand for automation and intelligent solutions.

INSIGHT:
Overall sentiment appears cautiously optimistic with solid growth prospects if execution remains strong.
Generated at: {now}
"""

    return {
        "analysis": analysis

    }
