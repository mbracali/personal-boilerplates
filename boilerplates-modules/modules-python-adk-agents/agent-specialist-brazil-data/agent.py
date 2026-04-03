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
    get_banks, 
    get_bank_by_code, 
    get_available_currencies, 
    get_exchange_rate, 
    get_cep_v1, 
    get_cep_v2, 
    get_cnpj_info, 
    get_all_brokers, 
    get_broker_by_cnpj, 
    get_cptec_cities, 
    search_cptec_city, 
    get_capital_weather, 
    get_airport_weather, 
    get_city_forecast, 
    get_ocean_forecast, 
    get_ddd_info, 
    get_holidays, 
    get_fipe_brands, 
    get_fipe_price, 
    get_fipe_reference_tables, 
    get_ibge_municipalities, 
    get_all_states, 
    get_state_info, 
    get_book_by_isbn, 
    get_all_ncms, 
    search_ncm, 
    get_ncm_by_code, 
    get_pix_participants, 
    check_domain_status, 
    get_financial_indicators, 
    get_indicator_by_name
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
brazilian_expert = Agent(
    model=azure_model,
    name=config['agent']['agent_name'],
    description=agent_description,
    instruction=agent_instructions,
    tools=[
        get_banks, get_bank_by_code, get_available_currencies,
        get_exchange_rate, get_cep_v1, get_cep_v2, get_cnpj_info,
        get_all_brokers, get_broker_by_cnpj, get_cptec_cities,
        search_cptec_city, get_capital_weather, get_airport_weather,
        get_city_forecast, get_ocean_forecast, get_ddd_info,
        get_holidays, get_fipe_brands,get_fipe_price,
        get_fipe_reference_tables, get_ibge_municipalities,
        get_all_states, get_state_info, get_book_by_isbn, get_all_ncms,
        search_ncm, get_ncm_by_code, get_pix_participants,
        check_domain_status, get_financial_indicators,
        get_indicator_by_name
    ],
    sub_agents=[]
)
