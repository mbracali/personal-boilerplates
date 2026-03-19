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

# Import all tools from the os_ops_topics.py
from .agent_tools.tools import (
    write_output_file,
    list_directory,
    read_file_content,
    search_files_by_pattern
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
os_operations_expert = Agent(
    model=azure_model,
    name=config['agent']['agent_name'],
    description=agent_description,
    instruction=agent_instructions,
    tools=[
        write_output_file,
        list_directory,
        read_file_content,
        search_files_by_pattern
    ],
    sub_agents=[],
)
