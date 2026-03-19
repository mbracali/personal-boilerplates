"""
Agent definitions for the research multi-agent system.

This is the root agent, responsible to coordinate other agents and 
routing between tasks.

The tools for this agent live inside the agent_tools folder
"""

# Standard imports
import os

# Data handling 
import tomllib

# ADK imports
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

# Import all tools from the brazil_topics.py
from .agent_tools.tools import (
    # --- Ticker: single symbol ---
    get_ticker_info,
    get_ticker_fast_info,
    get_ticker_history,
    get_ticker_actions,
    get_ticker_dividends,
    get_ticker_splits,
    get_ticker_financials,
    get_ticker_balance_sheet,
    get_ticker_cashflow,
    get_ticker_calendar,
    get_ticker_analyst_price_targets,
    get_ticker_earnings_estimate,
    get_ticker_revenue_estimate,
    get_ticker_earnings_history,
    get_ticker_eps_trend,
    get_ticker_growth_estimates,
    get_ticker_recommendations,
    get_ticker_upgrades_downgrades,
    get_ticker_major_holders,
    get_ticker_institutional_holders,
    get_ticker_mutual_fund_holders,
    get_ticker_options_dates,
    get_ticker_option_chain,
    get_ticker_news,
    # --- Search ---
    search_ticker,
    # --- Market summary ---
    get_market_status,
    get_market_summary,
    # --- Sector & Industry ---
    get_sector_overview,
    get_sector_top_companies,
    get_sector_top_etfs,
    get_industry_overview,
    get_industry_top_companies,
    get_industry_top_growth_companies,
    # --- Screener ---
    screen_equities,
)

# Get the base DIR
base_dir = os.path.dirname(os.path.abspath(__file__))

# Load config file
with open(f"{base_dir}/agent_docs/config.toml", "rb") as f:
    config = tomllib.load(f)

# Load markdown | Root agent
with open(f"{base_dir}/agent_docs/sub_agent_description.md", "r") as f:
    agent_description = f.read()

with open(f"{base_dir}/agent_docs/sub_agent_instructions.md", "r") as f:
    agent_instructions = f.read()

# Resolve active model profile from env (e.g. LOCAL_OLLAMA, AZURE_KIMIKV25)
_profile = os.getenv('ACTIVE_MODEL', 'LOCAL_OLLAMA')
_model_name = os.getenv(f'{_profile}_NAME')
_model_url  = os.getenv(f'{_profile}_URL')
_model_key  = os.getenv(f'{_profile}_KEY')

# Object instance | LiteLlm framework — model selected via ACTIVE_MODEL
azure_model = LiteLlm(
    model=_model_name,
    api_base=_model_url,
    api_key=_model_key,
    add_function_to_prompt=True,
    )

# Object instance | ADK agent using LiteLlm framework
finances_expert = Agent(
    model=azure_model,
    name=config['agent']['agent_name'],
    description=agent_description,
    instruction=agent_instructions,
    tools=[
        # Ticker – single symbol
        get_ticker_info,
        get_ticker_fast_info,
        get_ticker_history,
        get_ticker_actions,
        get_ticker_dividends,
        get_ticker_splits,
        get_ticker_financials,
        get_ticker_balance_sheet,
        get_ticker_cashflow,
        get_ticker_calendar,
        get_ticker_analyst_price_targets,
        get_ticker_earnings_estimate,
        get_ticker_revenue_estimate,
        get_ticker_earnings_history,
        get_ticker_eps_trend,
        get_ticker_growth_estimates,
        get_ticker_recommendations,
        get_ticker_upgrades_downgrades,
        get_ticker_major_holders,
        get_ticker_institutional_holders,
        get_ticker_mutual_fund_holders,
        get_ticker_options_dates,
        get_ticker_option_chain,
        get_ticker_news,
        # Search
        search_ticker,
        # Market summary
        get_market_status,
        get_market_summary,
        # Sector & Industry
        get_sector_overview,
        get_sector_top_companies,
        get_sector_top_etfs,
        get_industry_overview,
        get_industry_top_companies,
        get_industry_top_growth_companies,
        # Screener
        screen_equities,
    ],
    sub_agents=[]
)
